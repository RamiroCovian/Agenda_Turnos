########################################################################################
####################################### VALIDAR ########################################
########################################################################################

"""
validate.py:
    En este modulo se encuentra el codigo para realizar la validacion REGEX en los campos
    de obtencion de datos : Nombre, Apellido y Telefono. Y en caso de que no se pueda validar,
    presente Excepciones.
"""

import re
from my_exceptions import Errors


class Validate:
    def __init__(
        self,
    ):
        print("validar")

    def regex_(self, nombre, apellido, contacto):
        cadena = nombre.get()
        cadena1 = apellido.get()
        cadena2 = contacto.get()
        # Patron para validar los campos por REGEX
        patron = "^[A-Za-z\s áéíóú]*$"
        patron1 = "^[0-9]*$"  # Patron para validar los campos por REGEX
        if re.match(patron, cadena) and cadena != "":
            if re.match(patron, cadena1) and cadena1 != "":
                if re.match(patron1, cadena2) and cadena2 != "":
                    print("VALIDACION EXITOSA")
                else:
                    # Metodo personalizado de errores
                    Errors.error_("TELEFONO")
            else:
                Errors.error_("APELLIDO")
        else:
            Errors.error_("NOMBRE")
