import tkinter as tk
from controlador import ControladorEmpresa

if __name__ == "__main__":
    root = tk.Tk()
    app = ControladorEmpresa(root)
    root.mainloop()
