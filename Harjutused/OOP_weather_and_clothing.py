"""
Loo klassid Weather def __init__(self, temperature): ja Clothing def __init__(self, name, warmth_rating):
Pead tagastama meetodis def is_fit_for_temperature(self, temperature):, kas riideese on sobilik tänase temperatuuri jaoks.
Riideeseme warmth_rating peab olema kõrgem kui väistempetaruur.
Lõpus tagastada kas on sobilik vormis: *clothing* is/is not appropriate for *temeprature*
"""


class Clothing:
    def __init__(self, name, warmth_rating):
        self.name = name
        self.warmth_rating = warmth_rating

    def is_fit_for_temperature(self, temperature):
        if temperature < self.warmth_rating:
            return f"{self.name} is appropriate for {temperature}C"
        return f"{self.name} is not appropriate for {temperature}C"


class Weather:
    def __init__(self, temperature):
        self.temperature = temperature


sweater = Clothing("Sweater", 15)
current_weather = Weather(8)
print(sweater.is_fit_for_temperature(current_weather.temperature))
