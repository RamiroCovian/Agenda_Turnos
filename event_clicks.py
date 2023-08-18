########################################################################################
####################################### EVENTOS ########################################
########################################################################################

"""
event_clicks.py:
    Clase de Eventos personalizados para los entry.

"""

# Clase de eventos personalizados
class Evento:
    # Metodo para reescribir el texto como referencia por defecto en el campo, si no se encuentra posicionado en el.
    def out_entry_click_nombre(self, event, entry_nombre, text):
        if entry_nombre.get() == "":
            entry_nombre.insert(0, text)
            entry_nombre.config(fg="grey")
            print("Tiene que poner nombre")

    # Metodo que elimina el texto de referencia por defecto
    def in_entry_click_nombre(self, event, entry_nombre):
        if entry_nombre.get() != "":
            entry_nombre.delete(0, "end")
            entry_nombre.config(fg="black")
            print("Se cumple la funcion de eliminar nombre")

    # Metodo para reescribir el texto como referencia por defecto en el campo, si no se encuentra posicionado en el.
    def out_entry_click_apellido(self, event, entry_apellido, text):
        if entry_apellido.get() == "":
            entry_apellido.insert(0, text)
            entry_apellido.config(fg="grey")
            print("Tiene que poner apellido")

    # Metodo que elimina el texto de referencia por defecto
    def in_entry_click_apellido(self, event, entry_apellido):
        if entry_apellido.get() != "":
            entry_apellido.delete(0, "end")
            entry_apellido.config(fg="black")
            print("Se cumple la funcion de eliminar apellido")

    # Metodo para reescribir el texto como referencia por defecto en el campo, si no se encuentra posicionado en el.
    def out_entry_click_contacto(self, event, entry_contacto, text):
        if entry_contacto.get() == "":
            entry_contacto.insert(0, text)
            entry_contacto.config(fg="grey")
            print("Tiene que poner contacto")

    # Metodo que elimina el texto de referencia por defecto
    def in_entry_click_contacto(self, event, entry_contacto):
        if entry_contacto.get() != "":
            entry_contacto.delete(0, "end")
            entry_contacto.config(fg="black")
            print("Se cumple la funcion de eliminar contacto")
