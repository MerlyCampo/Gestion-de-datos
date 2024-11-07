import mysql.connector

class ModeloEmpresa:
    def __init__(self):
        try:
            # establecemos la conexión con la base de datos
            self.connection = mysql.connector.connect(
                host="localhost",       
                user="root",            
                password="",    
                database="unad"
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Conexión exitosa a la base de datos.")
        except Exception as e:
            print(f"Error de conexión: {e}")
            self.cursor = None

    def ConsultarEmpleado(self):
        try:
            if self.cursor:
                self.cursor.execute("SELECT * FROM empleados")
                return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar empleados: {e}")
            return []

    def AgregarEmpleado(self, nombre_apellido, no_celular, cargo_actual):
        try:
            if self.cursor:
                sentencia = "INSERT INTO empleados (NombresApellidos, NoCelular, CargoActual) VALUES (%s, %s, %s)"
                parametros = (nombre_apellido, no_celular, cargo_actual)
                self.cursor.execute(sentencia, parametros)
                self.connection.commit()
                print("Empleado agregado exitosamente.")
        except Exception as e:
            print(f"Error al insertar empleado: {e}")

    def EditarEmpleado(self, emp_id, nombre_apellido, no_celular, cargo_actual):
        try:
            if self.cursor:
                sentencia = "UPDATE empleados SET NombresApellidos = %s, NoCelular = %s, CargoActual = %s WHERE Id = %s"
                parametros = (nombre_apellido, no_celular, cargo_actual, emp_id)
                self.cursor.execute(sentencia, parametros)
                self.connection.commit()
                print("Empleado actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")

    def BorrarEmpleado(self, emp_id):
        try:
            if self.cursor:
                sentencia= "DELETE FROM empleados WHERE Id = %s"
                self.cursor.execute(sentencia, (emp_id,))
                self.connection.commit()
                print("Empleado eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")

    def Cerrar(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection.is_connected():
                self.connection.close()
                print("Conexión cerrada.")
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")


