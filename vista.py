import tkinter as tk
from tkinter import messagebox

class VistaEmpresa:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados")

        self.label_nombres = tk.Label(root, text="Nombres y Apellidos:")
        self.label_nombres.grid(row=0, column=0)
        self.entry_nombres = tk.Entry(root)
        self.entry_nombres.grid(row=0, column=1)

        self.label_celular = tk.Label(root, text="No. Celular:")
        self.label_celular.grid(row=1, column=0)
        self.entry_celular = tk.Entry(root)
        self.entry_celular.grid(row=1, column=1)

        self.label_cargo = tk.Label(root, text="Cargo Actual:")
        self.label_cargo.grid(row=2, column=0)
        self.entry_cargo = tk.Entry(root)
        self.entry_cargo.grid(row=2, column=1)

        #botones para las acciones
        self.boton_agregar = tk.Button(root, text="Agregar", command=self.AgregarEmpleado)
        self.boton_agregar.grid(row=3, column=0)

        self.boton_editar = tk.Button(root, text="Actualizar", command=self.EditarEmpleado)
        self.boton_editar.grid(row=3, column=1)

        self.boton_borrar = tk.Button(root, text="Eliminar", command=self.BorrarEmpleado)
        self.boton_borrar.grid(row=3, column=2)

        self.boton_consultar = tk.Button(root, text="Consultar", command=self.ConsultarEmpleado)
        self.boton_consultar.grid(row=4, column=0)

        #lista para mostrar los empleados
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=5, column=0, columnspan=3)

    def AgregarEmpleado(self):
        try:
            nombre_apellido = self.entry_nombres.get()
            no_celular = self.entry_celular.get()
            cargo_actual = self.entry_cargo.get()
            
            # Verificamos que los campos no estén vacíos
            if not nombre_apellido or not no_celular or not cargo_actual:
                raise ValueError("Todos los campos son obligatorios.")
            
            #llamamos al metodo del controlador para agregar empleado
            self.on_AgregarEmpleado(nombre_apellido, no_celular, cargo_actual)
        except ValueError as ve:
            messagebox.showerror("Error de entrada", f"Error: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar el empleado: {e}")

    def EditarEmpleado(self):
        try:
            emp_id, nombre_apellido, no_celular, cargo_actual = self.get_seleccionar_empleado()
            if emp_id:
                # Verificamos que los campos no estén vacíos
                if not nombre_apellido or not no_celular or not cargo_actual:
                    raise ValueError("Todos los campos son obligatorios.")
                self.on_EditarEmpleado(emp_id, nombre_apellido, no_celular, cargo_actual)
        except ValueError as ve:
            messagebox.showerror("Error de entrada", f"Error: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el empleado: {e}")

    def BorrarEmpleado(self):
        try:
            emp_id, _, _, _ = self.get_seleccionar_empleado()
            if not emp_id:
                raise ValueError("Debe seleccionar un empleado para eliminar.")
            self.on_BorrarEmpleado(emp_id)
        except ValueError as ve:
            messagebox.showerror("Error de entrada", f"Error: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el empleado: {e}")

    def ConsultarEmpleado(self):
        try:
            self.on_ConsultarEmpleado()
        except Exception as e:
            messagebox.showerror("Error", f"Error al consultar los empleados: {e}")

    def get_seleccionar_empleado(self):
        #Obtiene el empleado seleccionado en la lista
        seleccionar = self.listbox.curselection()
        if seleccionar:
            emp_id = self.listbox.get(seleccionar[0]).split()[0]  # Obtiene el ID del empleado
            nombre_apellido = self.entry_nombres.get()
            no_celular = self.entry_celular.get()
            cargo_actual = self.entry_cargo.get()
            return emp_id, nombre_apellido, no_celular, cargo_actual
        return None, None, None, None

    # Métodos de callback para que el controlador los asigne
    def on_AgregarEmpleado(self, nombre_apellido, no_celular, cargo_actual):
        pass

    def on_EditarEmpleado(self, emp_id, nombre_apellido, no_celular, cargo_actual):
        pass

    def on_BorrarEmpleado(self, emp_id):
        pass

    def on_ConsultarEmpleado(self):
        pass

    def MostrarEmpleado(self, empleados):
        #Muestra la lista de empleados en el listbox
        self.listbox.delete(0, tk.END)
        for emp in empleados:
            self.listbox.insert(tk.END, f"{emp[0]} {emp[1]} - {emp[2]} - {emp[3]}")
