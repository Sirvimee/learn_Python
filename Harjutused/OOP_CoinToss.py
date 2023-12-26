"""
Ette on antud klass CoinToss, mille play() meetotod genereerib kas võidu või kaotuse.
Loo klass nimega Player def __init__(self, name, balance):, mis kutsub välja meetodis def play_game(), CoinToss mängu.
Kui mängijal pole piisavalt raha mängimiseks tagastada "Not enough money for this bet".
Mängu mängimisel vastavalt tulemusele suurendada või vähendada Playeri rahakogust.
"""


class CoinToss:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def play(self) -> bool:
        import random
        return random.choice([True, False])


class Player:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

    def play_game(self, game: CoinToss, bet: int):
        if bet <= self.balance:
            if game.choice is True:
                self.balance += bet
            else:
                self.balance -= bet
        else:
            return "Not enough money for this bet"


player2 = Player("Bob", 30)
coin_toss = CoinToss("Coin Toss")
result = player2.play_game(coin_toss, 50)
print(result)
