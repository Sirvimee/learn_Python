"""
Klassid Dog ja DogShow.

Dog klassis on konstruktor, mis võtab vastu koera nime ja trikid, mida koer oskab.
DogShow klass korraldab koertenäituse, kus saab lisada koeri ja korraldada trikkide võistluse.
Meetod conduct_show kirjutab iga koera kohta tema nime ja milliseid trikke ta oskab.
Nt: Clyde esitab trikke: flip, dance.
"""


class Dog:
    def __init__(self, name: str, tricks: list):
        self.name = name
        self.tricks = tricks

class DogShow:
    def __init__(self, dogs: list):
        self.dogs = dogs

    def add_dog(self, dog: Dog) -> None:
        self.dogs.append(dog)

    def conduct_show(self) -> None:
        for dog in self.dogs:
            print(f"{dog.name} esitab trikke: {', '.join(dog.tricks)}")


dog1 = Dog("Clyde", ["flip", "dance"])
dog2 = Dog("Jenkins", ["jump", "crawl"])
show = DogShow([dog1, dog2])

print(dog1 in show.dogs)
print(dog2 in show.dogs)