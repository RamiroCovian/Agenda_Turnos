########################################################################################
#################################### OBSERVADORES ######################################
########################################################################################

"""
observer.py:
    Observadores personalizados que registran la cantidad de veces que se ejecutan
    acciones como: el registro de los datos.
"""


class Subject:
    observers = []

    def add(self, obj):
        self.observers.append(obj)

    def remove(self, obj):
        self.observers.remove(obj)

    def notify(self, *args):
        for observer in self.observers:
            observer.update(args)


class ObservConcrete(Subject):
    def __init__(self,):
        self.status = None

    def set_status(self, value):
        self.status = value
        self.notify()

    def get_status(self,):
        return self.status


class Observer:
    def update(self):
        raise NotImplementedError("Delegacion de actualizacion")


class ConcreteObserverA(Observer):
    def __init__(self, obj):
        self.observer_a = obj
        self.observer_a.add(self)

    def update(self, *args):
        print("Actualizacion dentro de ConcreteObserverA")
        print("Estos son los datos registrados: ", args)
