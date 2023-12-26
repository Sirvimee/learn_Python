"""
Looge klassid Painter ja ArtGallery. Painter klassil on atribuudid nimi ja maalide (sõnede) loend.
ArtGallery peaks suutma luua galerii, mis grupeerib maalid automaatselt kunstnike järgi, kasutades Painter
objektide nimekirja. ArtGallery konstruktorisse antakse kaasa järjend kunstnike objektidega.
Konstruktoris tuleb luua objekti muutuja gallery, mis on sõnastik, kus võtmeks on kõik kunstnike nimed ja
väärtusteks vastava kunstniku maalide nimed.
"""


class Painter:
    def __init__(self, name: str, paintings: list):
        self.name = name
        self.paintings = paintings


class ArtGallery:
    def __init__(self, painters: [Painter]):
        self.gallery = {}
        for painter in painters:
            self.gallery[painter.name] = painter.paintings


painter1 = Painter("Van Gogh", ["Starry Night", "Sunflowers"])
painter2 = Painter("Monet", ["Water Lilies", "Haystacks"])
gallery = ArtGallery([painter1, painter2])

print("Van Gogh" in gallery.gallery)
print("Starry Night" in gallery.gallery["Van Gogh"])


paintings_of_van_gogh = set(["Starry Night", "Sunflowers"])
gallery_paintings_of_van_gogh = set(gallery.gallery["Van Gogh"])

print(paintings_of_van_gogh == gallery_paintings_of_van_gogh)