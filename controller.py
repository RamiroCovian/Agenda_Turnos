########################################################################################
##################################### CONTROLADOR ######################################
########################################################################################

"""
controller.py:
    Controlador de la aplicacion.
"""

from tkinter import Tk
import view
import observer
import threading
from server import start_server
import subprocess
import sys
from logs import logs


theproc = ""


class Controller:
    def __init__(self, main):
        self.main_controller = main
        self.objeto_vista = view.Ventana(self.main_controller)
        self.the_observer = observer.ConcreteObserverA(
            self.objeto_vista.objeto_base)
        # Lanzo servidor
        if theproc != "":
            theproc.kill()
            threading.Thread(
                target=self.launch_server, args=(
                    self.objeto_vista.objeto_sql,), daemon=True
            ).start()
        else:
            threading.Thread(
                target=self.launch_server, args=(
                    self.objeto_vista.objeto_sql,), daemon=True
            ).start()

    def launch_server(self, var):

        the_path = start_server()
        if var == True:
            global theproc
            theproc = subprocess.Popen([sys.executable, the_path])
            theproc.communicate()


if __name__ == "__main__":
    main = Tk()
    aplicacion = Controller(main)
    aplicacion.objeto_vista.actualizar()
    main.mainloop()
