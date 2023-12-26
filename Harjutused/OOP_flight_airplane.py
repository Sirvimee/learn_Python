"""
Looge klassid Flight ja Airline. Flight klassil peab olema nimi ja lennu number,
Airline konstruktor peaks looma lennufirma, määrates lennud automaatselt etteantud Flight objektide nimekirja põhjal.
Lisa meetod add_flight selleks, et lisada lennud lennufirmasse.
"""


class Flight:
    def __init__(self, number: str, destination: str):
        self.destination = destination
        self.number = number

class Airline:
    def __init__(self, flights: [Flight]):
        self.flights = []
        for flight in flights:
            self.flights.append(flight)

    def add_flight(self, flight: Flight):
        self.flights.append(flight)


flight1 = Flight("LH123", "Frankfurt")
flight2 = Flight("BA456", "London")
airline = Airline([flight1, flight2])

print(flight1 in airline.flights)
print(flight2 in airline.flights)
