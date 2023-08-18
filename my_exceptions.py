########################################################################################
################################### MIS EXCEPCIONES ####################################
########################################################################################

"""
my_exceptions.py:
    En este modulo presento una clase Errores que posee herencia de la clase exception.
    La misma contiene metodos de registro de excepciones personalizadas. Los errores que se registrarian
    por parte del metodo error_(), son de los campos en los que posean Patron para validar por REGEX y por parte
    del metodo error_index(), se regitrarian los errores al no seleccionar en el treeview el turno a cancelar. 
    Estos errores se guardaran en un archivo (.log), en este caso llamado logs&errors.log 
"""

import datetime
import logging


class Errors(Exception):
    # Metodo que registra en el archivo "errors.log" errores en la carga de datos.
    def error_(campo):
        logging.basicConfig(filename="logs&errors.log", level=logging.ERROR)
        logging.error(
            f"NO INGRESA {campo} CORRECTAMENTE. " + "Fecha: " + str(datetime.datetime.today().strftime("%d/%m/%y")) + " Hora: " + str(datetime.datetime.today().strftime("%H:%M:%S")) + "\n")
        # Excepcion personalizada
        raise Exception(f"NO INGRESA {campo} CORRECTAMENTE")

    # Metodo que registra en el archivo "errors.log", errores en la eliminacion de turnos.
    def error_index():
        logging.basicConfig(filename="logs&errors.log", level=logging.ERROR)
        logging.error(
            f"NO SELECCIONA EL TURNO A CANCELAR. " + "Fecha: " + str(datetime.datetime.today().strftime("%d/%m/%y")) + " Hora: " + str(datetime.datetime.today().strftime("%H:%M:%S")) + "\n")
        raise TypeError(
            "DEBE SELECCIONAR EL TURNO A CANCELAR"
        )  # Excepcion TypeError personalizada
