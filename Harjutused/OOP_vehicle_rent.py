"""
Loo klassid Vehicle ning RentalAgency. Vehicle klassi loo meetodi def rent() ning def return_vehicle(),
mis kontrollivad, kas autod on olemas ning neid saab rentida või on juba välja renditud ning kas neid saab tagastada.
RentalAgency klassi tuleb luua meetodid def add_vehicles(), millega lisada uusi autosid rendifirmasse ning
def rent_vehicle() ja def return_vehicle() millega läbi Vehicle klassi rentida ja tagastada autosid.
"""


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.available = True

    def rent(self):
        if self.available:
            self.available = False

    def return_vehicle(self):
        if not self.available:
            self.available = True


class RentalAgency:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def rent_vehicle(self, make, model):
        for vehicle in self.vehicles:
            if vehicle.make == make and vehicle.model == model:
                if vehicle.available:
                    vehicle.rent()
                    return "Vehicle rented"
                else:
                    return "Cannot rent vehicle"
        return "Vehicle not found"

    def return_vehicle(self, make, model):
        for vehicle in self.vehicles:
            if vehicle.make == make and vehicle.model == model:
                vehicle.return_vehicle()
                return "Vehicle returned"


car4 = Vehicle("Honda", "Civic")

rental_agency3 = RentalAgency()

rental_agency3.add_vehicle(car4)

print(rental_agency3.rent_vehicle("Toyota", "Corolla"))
print(rental_agency3.rent_vehicle("Opel", "Calibra"))
