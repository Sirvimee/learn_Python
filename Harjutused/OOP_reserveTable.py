"""
Lisa meetod reserve_table, mis saab laua numbri ning vaatab kui selline number on olemas ja kas laud on vaba
(kasuta meetodit reserve). Kui lauda saab broneerida, tuleb see broneerida ja tagastada True,
muul juhul tagastada False.
"""


class Table:
    def __init__(self, number: int, seats: int):
        self.number = number
        self.seats = seats
        self.reserved = False

    def reserve(self):
        self.reserved = True


class Restaurant:
    def __init__(self):
        self.tables = []

    def add_table(self, table: Table):
        self.tables.append(table)

    def reserve_table(self, number: int) -> bool:
        for table in self.tables:
            if table.number == number:
                if not table.reserved:
                    table.reserve()
                    return True
        return False


restaurant = Restaurant()
table1 = Table(1, 4)
restaurant.add_table(table1)
print(True == restaurant.reserve_table(1))
print(table1.reserved)

restaurant = Restaurant()
print(restaurant.reserve_table(1))
table1 = Table(1, 4)
restaurant.add_table(table1)
print(restaurant.reserve_table(2))