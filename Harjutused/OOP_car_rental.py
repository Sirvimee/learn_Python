"""
Klassid Vehicle ja RentalService. RentalService peaks suutma hallata sõidukite laenutust, kusjuures iga Vehicle
objekt sisaldab teavet sõiduki kohta ning laenutusstaatust.

Kui sõiduk on olemas ja seda saab laenutada (pole veel laenutatud),
siis rent_vehicle tagastab "[make] [model] is not booked". Muul juhul tagastab "[make] [model] is not available
"""


class Vehicle:
    def __init__(self, make: str, model: str, available: bool=True):
        self.make = make
        self.model = model
        self.available = available


class RentalService:
    def __init__(self, vehicles: list[Vehicle]):
        self.vehicles = {(v.make, v.model): v for v in vehicles}

    def rent_vehicle(self, make: str, model: str):
        if (make, model) in self.vehicles:
            vehicle = self.vehicles[(make, model)]
            if vehicle.available:
                vehicle.available = False
                return f"{vehicle.make} {vehicle.model} is now booked"
            else:
                return f"{vehicle.make} {vehicle.model} is not available"
        else:
            return f"{make} {model} is not available"


vehicle1 = Vehicle("Toyota", "Corolla")
vehicle2 = Vehicle("Honda", "Civic")
service = RentalService([vehicle1, vehicle2])
print(service.rent_vehicle("Toyota", "Corolla"))