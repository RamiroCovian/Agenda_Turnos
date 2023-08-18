#######################################################################################
################################ FUNCIONES DE BOTONES #################################
#######################################################################################
"""
function_buttons.py:
    En este modulo se encontraran dentro de la clase FuntionButton los
    metodos que llevaran a cabo todas las acciones de nuestra aplicacion: Reserva de turno,
    Cancelacion de turno, Modificacion de turno, Consulta, entre otras
"""

from tkinter.colorchooser import askcolor
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter import END
from validate import Validate
from model import Crud
from my_exceptions import Errors
from observer import Subject
from controller import theproc
from logs import close_logs


class FunctionButton(Subject):
    def __init__(
        self,
    ):
        pass

    # Metodo para agregar una fila de dato en mi tabla

    def funcion_reserva(self, fecha, hora, nombre, apellido, contacto, tree):
        try:
            Validate.regex_(self, nombre, apellido, contacto)
            Crud.reserva(
                self, fecha, hora, nombre, apellido, contacto)
            # Actualizo Treeview, donde se observan los registros
            Crud.actualizar_treeview(self, tree)
            showinfo(Crud.titulo_app, "Turno reservado")
            print("RESERVA EXITOSA")
            # Metodo de notificacion del Observador
            self.notify(fecha.get_date(), hora.get(), nombre.get(),
                        apellido.get(), contacto.get())
        except:
            showerror(
                "¡¡Atencion!",
                "¡Lo datos ingresados no son los correctos!",
            )

    # Metodo para eliminar una fila de dato en mi tabla

    def funcion_cancelar(self, tree):
        try:
            if askyesno(
                "¡Atencion!",
                "Usted esta a punto de cancelar el turno, ¿Desea continuar?",
            ):
                Crud.cancel(
                    self, tree)
                showinfo(Crud.titulo_app, "¡Turno cancelado!")
                Crud.actualizar_treeview(self, tree)
                print("CANCELACION EXITOSA")
            else:
                showinfo(Crud.titulo_app, "¡El turno no se cancelo!")
        except:
            showinfo(Crud.titulo_app,
                     "¡Seleccione turno a cancelar!")
            Errors.error_index()  # Metodo personalizado de errores

    # Metodo para modificar fila de datos en mi tabla

    def funcion_modificar(self, fecha, hora, nombre, apellido, contacto, tree):
        try:
            if askyesno("¡Atencion!", "¿Desea modificar los datos?"):
                Validate.regex_(self, nombre, apellido, contacto)
                Crud.modify(self, fecha, hora, nombre,
                            apellido, contacto, tree)
                Crud.actualizar_treeview(self, tree)
                showinfo(Crud.titulo_app, "Modificacion exitosa")
                print("MODIFICACION EXITOSA")
            else:
                showinfo(Crud.titulo_app, "¡Modificacion cancelada!")
        except:
            showerror(
                "¡¡Atencion!",
                "¡Lo datos ingresados no son los correctos!",
            )

    # Metodo para salir de la aplicacion

    def funcion_salir(self, main):
        if askyesno("Atencion", "¿Esta seguro que desea salir?"):
            main.quit()
            print("CIERRE DE PROGRAMA")
            close_logs.close_main()

    # Metodo para elegir color de fondo

    def funcion_color(self, main):
        resultado = askcolor(color="#00ff00", title="Elija color")
        main.config(bg=resultado[1])
