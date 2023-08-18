#######################################################################################
####################################### MODELO ########################################
#######################################################################################
"""
model.py:
    En este modulo se encuentran las estructuras y metodos para la creacion
    de nuestra Base de Dato, junto con su tabla, atributos y sus respectivos TypeField.
"""

from peewee import *
from decorators import new_reserve
from decorators import new_cancel
from decorators import new_modify

try:
    db = SqliteDatabase("turnos.db")
except:
    print("No se pudo crear la base de datos")


class BaseModel(Model):
    class Meta:
        database = db  # Este Model usara "turnos.dp" como base de dato.


# La clase Agenda es la tabla donde se almacenaran los datos.
class Agenda(BaseModel):
    id = IntegerField(unique=True, primary_key=True)
    fecha = DateTimeField()
    hora = TimeField()  # hora(atributo), TimeField()(Type Field)
    nombre = CharField()
    apellido = CharField()
    contacto = IntegerField()


class Crud:
    def __init__(
        self,
    ):
        self.con = db
        self.con.connect()  # Conexion con la base de datos.
        self.con.create_tables([Agenda])  # Creo la tabla en la base de datos.

    el_id = 0
    titulo_app = "Syntia Terapeuta"

    # Decorador personalizado, Contador de nuevos registros realizados
    @new_reserve
    # Metodo para agregar una fila de dato en mi tabla
    def reserva(self, fecha, hora, nombre, apellido, contacto):
        agenda = Agenda()
        agenda.fecha = fecha.get_date()
        agenda.hora = hora.get()
        agenda.nombre = nombre.get()
        agenda.apellido = apellido.get()
        agenda.contacto = contacto.get()
        agenda.save()  # Guardo registro de datos en la tabla

    # Metodo para actualizar Treeview
    def actualizar_treeview(self, tree):
        records = tree.get_children()
        for element in records:
            tree.delete(element)

        for fila in Agenda.select().order_by(
            Agenda.fecha.asc(),
            Agenda.hora.asc(),
        ):
            tree.insert(
                "",
                "end",
                text=fila.id,
                values=(
                    fila.fecha,
                    fila.hora,
                    fila.nombre,
                    fila.apellido,
                    fila.contacto,
                ),
            )

    # Decorador personalizado, Contador de cancelacion de registros realizados
    @new_cancel
    # Metodo para cancelar datos seleccionados en el Treeview
    def cancel(self, tree):
        valor = tree.selection()
        item = tree.item(valor)
        cancelar = Agenda.get(Agenda.id == item["text"])
        cancelar.delete_instance()  # Elimino registro seleccionado de la tabla

    # Decorador personalizado, Contador de modificaciones de registros realizados
    @new_modify
    # Metodo para modificar datos seleccionados en el Treeview
    def modify(self, fecha, hora, nombre, apellido, contacto, tree):
        valor = tree.selection()
        item = tree.item(valor)
        actualizar = Agenda.update(
            fecha=fecha.get_date(),
            hora=hora.get(),
            nombre=nombre.get(),
            apellido=apellido.get(),
            contacto=contacto.get(),
        ).where(Agenda.id == item["text"])
        actualizar.execute()  # Actualizo registro de la fila seleccionada

    # Metodo para consutar registros de datos de mi tabla
    def consult(self, tree):
        self.actualizar_treeview(tree)
        print("CONSULTA EXITOSA")
