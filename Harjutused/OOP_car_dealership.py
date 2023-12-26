"""
Klassil Car on mark (make), mudel (model) ja hind. Klassi Dealership kirjuta meetod find_car, mis leiab ja tagastab
auto margi ja mudeli alusel, kui sellist autot pole, tagastab None
"""


class Car:
    def __init__(self, make: str, model: str, price: int):
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.make} {self.model} priced at ${self.price}"

class Dealership:
    def __init__(self, name: str):
        self.name = name
        self.inventory = []

    def add_car(self, car: Car):
        self.inventory.append(car)

    def find_car(self, make: str, model: str) -> Car:
        for car in self.inventory:
            if car.make == make and car.model == model:
                return car


car2 = Car("Honda", "Civic", 22000)
dealership = Dealership("City Motors")
dealership.add_car(car2)

found_car = dealership.find_car("Honda", "Civic")
print(found_car == car2)