########################################################################################
######################################## VISTA #########################################
########################################################################################

"""
view.py:
    En este modulo se encuentra todo el codigo necesario para darle una vista a
    nuestra aplicacion y poder interactuar con ella.
"""

from tkinter import ttk
from tkinter import Tk
from tkinter import StringVar
from tkinter import LabelFrame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Menu
from tkinter import ttk
from tkinter import W
from tkinter import E
from tkinter import S
from tkinter import N
from tkinter import END
from tkcalendar import Calendar
import datetime
from function_buttons import FunctionButton
from event_clicks import Evento
from model import Crud

# Clase en donde se configura la ventana, botones, menu, calendario y treeview


class Ventana:
    def __init__(self, window):
        self.objeto_base = FunctionButton()
        self.objeto_event = Evento()
        self.objeto_sql = Crud()

        # Configuracion Ventana
        self.main = window
        self.main.title(self.objeto_sql.titulo_app)  # Titulo de App
        self.main.geometry("685x608")  # Dimensiones
        self.main.resizable(
            width=False, height=False
        )  # Metodo que no permite modificar tamaño
        self.main.iconbitmap("icono.ico")  # Icono de App
        self.main.configure(bg="#A1A1F1")  # Color de fondo

        # Variables
        self.var_nombre = StringVar()
        self.var_apellido = StringVar()
        self.var_celular = StringVar()

        # Recuadro para contener etiquetas
        recuadro = LabelFrame(
            self.main, text="Registro de Personas", bg="#A1A1F1")
        recuadro.grid(row=0, column=0, pady=30, padx=10)

        # Etiquetas
        nombre = Label(recuadro, text="Nombre", width=25, bg="#A1A1F1")
        nombre.grid(row=0, column=1, sticky=W, pady=10)
        apellido = Label(recuadro, text="Apellido", width=25, bg="#A1A1F1")
        apellido.grid(row=1, column=1, sticky=W, pady=10)
        contacto = Label(recuadro, text="Telefono", width=25, bg="#A1A1F1")
        contacto.grid(row=2, column=1, sticky=W, pady=10)
        fecha = Label(recuadro, text="Fecha", width=25, bg="#A1A1F1")
        fecha.grid(row=3, column=1, sticky=W, pady=10)
        hora = Label(recuadro, text="Horario", width=25, bg="#A1A1F1")
        hora.grid(row=4, column=1, sticky=W, pady=10)

        # Campos para completar datos
        entry_nombre = Entry(recuadro, textvariable=self.var_nombre, width=25)
        entry_nombre.grid(row=0, column=2, sticky=W)
        entry_nombre.config(fg="grey")
        entry_nombre.insert(0, "-Ingrese un Nombre-")
        entry_nombre.bind(
            "<FocusIn>",
            lambda event: self.objeto_event.in_entry_click_nombre(
                event, entry_nombre),
        )
        entry_nombre.bind(
            "<FocusOut>",
            lambda event: self.objeto_event.out_entry_click_nombre(
                event, entry_nombre, "-Ingrese un Nombre-"
            ),
        )

        entry_apellido = Entry(
            recuadro, textvariable=self.var_apellido, width=25)
        entry_apellido.grid(row=1, column=2, sticky=W)
        entry_apellido.config(fg="grey")
        entry_apellido.insert(0, "-Ingrese un Apellido-")

        entry_apellido.bind(
            "<FocusIn>",
            lambda event: self.objeto_event.in_entry_click_apellido(
                event, entry_apellido
            ),
        )
        entry_apellido.bind(
            "<FocusOut>",
            lambda event: self.objeto_event.out_entry_click_apellido(
                event, entry_apellido, "-Ingrese un Apellido-"
            ),
        )
        entry_contacto = Entry(
            recuadro,
            textvariable=self.var_celular,
            width=25,
        )
        entry_contacto.grid(row=2, column=2, sticky=W)
        entry_contacto.config(fg="grey")
        entry_contacto.insert(0, "-Sin espacios y sin simbolos-")

        entry_contacto.bind(
            "<FocusIn>",
            lambda event: self.objeto_event.in_entry_click_contacto(
                event, entry_contacto
            ),
        )
        entry_contacto.bind(
            "<FocusOut>",
            lambda event: self.objeto_event.out_entry_click_contacto(
                event, entry_contacto, "-Sin espacios y sin simbolos-"
            ),
        )

        # ComboBox para seleccionar hora
        combo = ttk.Combobox(
            recuadro,
            state="readonly",
            values=[
                "9:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "15:00",
                "16:00",
                "17:00",
                "18:00",
                "19:00",
            ],
        )
        combo.set("Seleccione Hora")
        combo.grid(row=4, column=2, sticky=W)

        ########################################################################################
        ####################################### BOTONES ########################################
        ########################################################################################

        boton_guardar = Button(
            recuadro,
            text="Reservar Turno",
            width=25,
            command=lambda: self.objeto_base.funcion_reserva(
                tkc,
                combo,
                self.var_nombre,
                self.var_apellido,
                self.var_celular,
                self.tree,
            ),
            bg="#847BF6",
        )
        boton_guardar.grid(row=5, column=1, sticky=W + E)

        boton_consultar = Button(
            recuadro,
            text="Consultar",
            width=25,
            command=lambda: self.objeto_sql.consult(self.tree),
            bg="#847BF6",
        )
        boton_consultar.grid(row=6, column=1, sticky="w")

        boton_eliminar = Button(
            recuadro,
            text="Cancelar Turno",
            width=25,
            command=lambda: self.objeto_base.funcion_cancelar(self.tree),
            bg="#847BF6",
        )
        boton_eliminar.grid(row=6, column=2, sticky=W + E)

        boton_modificar = Button(
            recuadro,
            text="Modificar",
            width=25,
            command=lambda: self.objeto_base.funcion_modificar(
                tkc,
                combo,
                self.var_nombre,
                self.var_apellido,
                self.var_celular,
                self.tree,
            ),
            bg="#847BF6",
        )
        boton_modificar.grid(row=5, column=2, sticky="w")

        boton_salir = Button(
            self.main,
            text="Salir",
            width=25,
            command=lambda: self.objeto_base.funcion_salir(self.main),
            bg="#FFAAFF",
        )
        boton_salir.grid(row=7, column=0, columnspan=9, sticky=W + E)

        ########################################################################################
        ######################################### MENU #########################################
        ########################################################################################

        menubar = Menu(self.main)

        menu_archivo = Menu(menubar, tearoff=0)
        menu_archivo.add_command(
            label="Reservar Turno",
            command=lambda: self.objeto_base.funcion_reserva(
                tkc,
                combo,
                self.var_nombre,
                self.var_apellido,
                self.var_celular,
                self.tree,
            ),
        )
        menu_archivo.add_command(
            label="Cancelar Turno",
            command=lambda: self.objeto_base.funcion_cancelar(self.tree),
        )
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label="Consultar Turnos",
            command=lambda: self.objeto_sql.consult(self.tree),
        )
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label="Salir", command=lambda: self.objeto_base.funcion_salir(self.main)
        )
        menubar.add_cascade(label="Archivo", menu=menu_archivo)

        menu_edicion = Menu(menubar, tearoff=0)
        menu_edicion.add_command(
            label="Modificar Datos",
            command=lambda: self.objeto_base.funcion_modificar(
                tkc,
                combo,
                self.var_nombre,
                self.var_apellido,
                self.var_celular,
                self.tree,
            ),
        )
        menu_edicion.add_separator()
        menubar.add_cascade(label="Editar", menu=menu_edicion)

        submenu = Menu(menu_edicion, tearoff=0)
        submenu.add_command(
            label="Color de fondo",
            command=lambda: self.objeto_base.funcion_color(self.main),
        )
        menu_edicion.add_cascade(label="Otros", menu=submenu)

        self.main.config(menu=menubar)

        ########################################################################################
        #################################### CALENDARIO ########################################
        ########################################################################################

        fecha_actual = datetime.datetime.now()
        recuadro_calendario = LabelFrame(
            self.main, text="Calendario", bg="#A1A1F1")
        recuadro_calendario.grid(row=0, column=1, pady=30, padx=10)

        tkc = Calendar(
            recuadro_calendario,
            selectmode="day",
            year=fecha_actual.year,
            month=fecha_actual.month,
            date=fecha_actual.day,
            date_pattern="dd-mm-yyyy",
        )
        tkc.grid(row=0, column=0)
        tkc.selection_set(fecha_actual.date())

        def funcion_fecha():
            date.config(text=tkc.get_date())

        boton_seleccionar = Button(
            recuadro_calendario,
            text="Seleccionar fecha",
            command=lambda: funcion_fecha(),
            bg="#847BF6",
        )
        boton_seleccionar.grid(row=1, column=0, sticky=W + E)
        date = Label(
            recuadro,
            text="Seleccione fecha en calendario",
            bg="black",
            fg="yellow",
        )
        date.grid(row=3, column=2, sticky="w")

        ########################################################################################
        ###################################### TREEVIEW ########################################
        ########################################################################################

        self.tree = ttk.Treeview(self.main)
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.tree.column("#0", width=20, minwidth=10, anchor="w")
        self.tree.column("col1", width=70, minwidth=60)
        self.tree.column("col2", width=90, minwidth=80)
        self.tree.column("col3", width=90, minwidth=80)
        self.tree.column("col4", width=90, minwidth=50)
        self.tree.column("col5", width=90, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Fecha")
        self.tree.heading("col2", text="Hora")
        self.tree.heading("col3", text="Nombre")
        self.tree.heading("col4", text="Apellido")
        self.tree.heading("col5", text="Contacto")
        self.tree.grid(row=1, column=0, columnspan=2, sticky=W + E)

        self.scrollbar = ttk.Scrollbar(
            self.main, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=6, columnspan=2, sticky=N + S + E)

    def actualizar(
        self,
    ):
        self.objeto_sql.actualizar_treeview(self.tree)
