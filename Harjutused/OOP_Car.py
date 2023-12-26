"""Loo klass Car ning mis sisaldab meetodit start_car(). See prindib konsooli "Engine started"."""


class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()


my_car = Car()
my_car.start_car()
