from modelo import ModeloEmpresa
from vista import VistaEmpresa

class ControladorEmpresa:
    def __init__(self, root):
        self.modelo = ModeloEmpresa()
        self.vista = VistaEmpresa(root)
        # Conectamos las funciones del controlador con la vista
        self.vista.on_AgregarEmpleado = self.AgregarEmpleado
        self.vista.on_EditarEmpleado = self.EditarEmpleado
        self.vista.on_BorrarEmpleado = self.BorrarEmpleado
        self.vista.on_ConsultarEmpleado = self.ConsultarEmpleado

    def ConsultarEmpleado(self):
        try:
            empleados = self.modelo.ConsultarEmpleado()
            self.vista.MostrarEmpleado(empleados)
        except Exception as e:
            print(f"Error al consultar empleados: {e}")
            self.vista.MostrarEmpleado([])

    def AgregarEmpleado(self, nombre_apellido, no_celular, cargo_actual):
        try:
            self.modelo.AgregarEmpleado(nombre_apellido, no_celular, cargo_actual)
            self.ConsultarEmpleado()  # Actualiza la lista de empleados
        except Exception as e:
            print(f"Error al agregar el empleado: {e}")

    def EditarEmpleado(self, emp_id, nombre_apellido, no_celular, cargo_actual):
        try:
            self.modelo.EditarEmpleado(emp_id, nombre_apellido, no_celular, cargo_actual)
            self.ConsultarEmpleado()  # Actualiza la lista de empleados
        except Exception as e:
            print(f"Error al actualizar el empleado: {e}")

    def BorrarEmpleado(self, emp_id):
        try:
            self.modelo.BorrarEmpleado(emp_id)
            self.ConsultarEmpleado()  # Actualiza la lista de empleados
        except Exception as e:
            print(f"Error al eliminar el empleado: {e}")

    def cerrar(self):
        try:
            self.modelo.cerrar()
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")
