"""
Luua klassid Person def __init__(self, name, money) ja Item def __init__(self, name, price).
Ning luua Person klassi sisse meetod buy_item. Buy_item tagastab True, kui Person objektil on piisavalt raha,
et osta Item ning false, kui ei ole. Kui Item on ostetud, väheneb Person raha.
"""


class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def buy_item(self, item=None):
        if self.money >= item.price:
            self.money -= item.price
            return True
        return False


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


person1 = Person("Alice", 100)
person2 = Person("Bob", 50)

item1 = Item("Phone", 80)
item2 = Item("Headphones", 30)

person1.buy_item(item1)
person2.buy_item(item2)
person1.buy_item(item2)

print(person1.money)
print(person2.money)