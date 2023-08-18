########################################################################################
##################################### DECORADORES ######################################
########################################################################################

"""
decorators.py:
    Decoradores personalizados que registran la cantidad de veces que se ejecutan
    acciones como: reserve, cancel o modify.
"""

import datetime


def new_reserve(function):
    def envelope(*args, **kwargs):
        envelope.number_reserve += 1
        archivo = open("user_records.txt", "a", encoding="utf-8")
        archivo.write(
            "Se han registrado un total de %s reservas. " %
            (envelope.number_reserve)
            + "Fecha: "
            + str(datetime.datetime.today().strftime("%d/%m/%y"))
            + " Hora: "
            + str(datetime.datetime.today().strftime("%H:%M:%S"))
            + "\n"
        )
        print("Se han registrado un total de %s reservas" %
              (envelope.number_reserve))
        return function(*args, **kwargs)

    envelope.number_reserve = 0
    return envelope


def new_cancel(function):
    def envelope(*args, **kwargs):
        envelope.number_cancel += 1
        archivo = open("user_records.txt", "a", encoding="utf-8")
        archivo.write(
            "Se han cancelado un total de %s turnos. " %
            (envelope.number_cancel)
            + "Fecha: "
            + str(datetime.datetime.today().strftime("%d/%m/%y"))
            + " Hora: "
            + str(datetime.datetime.today().strftime("%H:%M:%S"))
            + "\n"
        )
        print("Se han cancelado un total de %s turnos" %
              (envelope.number_cancel))
        return function(*args, **kwargs)

    envelope.number_cancel = 0
    return envelope


def new_modify(function):
    def envelope(*args, **kwargs):
        envelope.number_modify += 1
        archivo = open("user_records.txt", "a", encoding="utf-8")
        archivo.write(
            "Se han registrado %s modificaciones de turnos. " %
            (envelope.number_modify)
            + "Fecha: "
            + str(datetime.datetime.today().strftime("%d/%m/%y"))
            + " Hora: "
            + str(datetime.datetime.today().strftime("%H:%M:%S"))
            + "\n"
        )
        print("Se han registrado %s modificaciones de turno" %
              (envelope.number_modify))
        return function(*args, **kwargs)

    envelope.number_modify = 0
    return envelope
