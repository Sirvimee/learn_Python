"""
Loo klass Owner, kellel on nimi ja list "pets" tema kõikidest lemmikloomadest.
Loo klass Pet, kellel on nimi ja liik.__eq__ peab tagastama, kas lemmikloomal ning tema omanikul on sama nimi.
"""


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(Pet(pet.name, pet.species))

    def __eq__(self, other):
        return self.name == other.name


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species


owner4 = Owner("Chris")
pet5 = Pet("Chris", "Dog")

print(owner4 == pet5)