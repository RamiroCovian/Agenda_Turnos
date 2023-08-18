########################################################################################
######################################### LOGS #########################################
########################################################################################

"""
logs.py:
    Logs personalizados que registran la apertura de conexion con el servidor y el cierre de la misma.
    Estos son registrados en un archivo (.log), en este caso llamado logs&errors.log
"""


import logging
import datetime


class logs:
    def main():
        logging.basicConfig(filename="logs&errors.log", level=logging.INFO)

        host = "192.168.1.13"
        port = 9999

        logging.info(f"El IP {host} con puerto {port} inicia conexion con el servidor. " + "Fecha: " + str(datetime.datetime.today().strftime("%d/%m/%y"))
                     + " Hora: "
                     + str(datetime.datetime.today().strftime("%H:%M:%S"))
                     + "\n")

    main()


class close_logs:
    def close_main():
        logging.basicConfig(filename="logs&errors.log", level=logging.INFO)

        host = "192.168.1.13"
        port = 9999

        logging.info(f"El IP {host} con puerto {port} cierra conexion con el servidor. " + "Fecha: " + str(datetime.datetime.today().strftime("%d/%m/%y"))
                     + " Hora: "
                     + str(datetime.datetime.today().strftime("%H:%M:%S"))
                     + "\n")

    close_main()
