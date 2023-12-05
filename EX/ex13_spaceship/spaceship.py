""" Spaceship."""


class Crewmate:
    """Crewmate class."""

    def __init__(self, color: str, role: str, tasks: int = 10):
        self.color = color.title()
        self.role = role.title()
        self.tasks = tasks
        self.roles = ["Crewmate", "Sheriff", "Guardian Angel", "Altruist"]
        self.protected = False

        if self.role not in self.roles:
            self.role = "Crewmate"

    def __repr__(self):
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        self.tasks -= 1


class Impostor:
    """Impostor class."""

    def __init__(self, color: str):
        self.color = color.capitalize()
        self.kills = 0

    def __repr__(self):
        return f"Impostor {self.color}, kills: {self.kills}."


class Spaceship:
    """Spaceship class."""

    def __init__(self):
        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []

    def get_crewmate_list(self):
        if len(self.crewmate_list) > 0:
            crewmates = ", ".join(crewmate.color for crewmate in self.crewmate_list[0: len(self.crewmate_list) - 1])
            last_crewmate = self.crewmate_list[-1].color
            return f"{crewmates} and {last_crewmate}"
        return self.crewmate_list

    def get_impostor_list(self):
        if len(self.impostor_list) > 0:
            impostors = ", ".join(impostor.color for impostor in self.impostor_list[0: len(self.impostor_list) - 1])
            last_impostor = self.impostor_list[-1].color
            return f"{impostors} and {last_impostor}"
        return self.impostor_list

    def get_dead_players(self):
        return ", ".join(player.color for player in self.dead_players)

    def add_crewmate(self, crewmate):
        if not isinstance(crewmate, Impostor):
            if crewmate not in self.crewmate_list and crewmate not in self.impostor_list:
                self.crewmate_list.append(crewmate)

    def add_impostor(self, impostor):
        if not isinstance(impostor, Crewmate):
            if (impostor.color not in [c.color for c in self.crewmate_list] and
                    impostor.color not in [c.color for c in self.impostor_list]):
                if len(self.impostor_list) < 3:
                    self.impostor_list.append(impostor)

    def kill_impostor(self, sheriff: Crewmate, color: str):
        if sheriff.role == "Sheriff":
            if color.title() in self.impostor_list:
                self.impostor_list.remove(color.title())
                self.dead_players.append(color.title())
            else:
                self.dead_players.append(sheriff)

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        self.crewmate_list.append(dead_crewmate)
        self.dead_players.remove(dead_crewmate)
        self.dead_players.append(altruist)
        self.crewmate_list.remove(altruist)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        if guardian_angel.role == "Guardian Angel" and guardian_angel in self.dead_players:
            count = 0
            for crewmate in self.crewmate_list:
                if crewmate.protected:
                    count += 1
            if count == 0:
                crewmate_to_protect.protected = True

    def kill_crewmate(self, impostor: Impostor, color: str):
        for crewmate in self.crewmate_list:
            if crewmate.color == color.title():
                if crewmate.protected:
                    crewmate.protected = False
                else:
                    self.crewmate_list.remove(crewmate)
                    self.dead_players.append(crewmate)
                    impostor.kills += 1

    def sort_crewmates_by_tasks(self):
        sorted_crewmates = sorted(self.crewmate_list, key=lambda x: x.tasks)
        return ", ".join(crewmate.color for crewmate in sorted_crewmates)

    def sort_impostors_by_kills(self):
        sorted_impostors = sorted(self.impostor_list, key=lambda x: x.kills, reverse=True)
        return ", ".join(impostor.color for impostor in sorted_impostors)

    def get_regular_crewmates(self):
        regular_crewmates = []
        for crewmate in self.crewmate_list:
            if crewmate.role == "Crewmate":
                regular_crewmates.append(crewmate)
        return ", ".join(crewmate.color for crewmate in regular_crewmates)

    def get_role_of_player(self, color: str):
        for crewmate in self.crewmate_list:
            if crewmate.color == color.title():
                return crewmate.role
        if color.title() in self.impostor_list:
            return "Impostor"

    def get_crewmate_with_most_tasks_done(self):
        crewmate_with_most_tasks = spaceship.sort_crewmates_by_tasks()[0]
        return crewmate_with_most_tasks

    def get_impostor_with_most_kills(self):
        impostor_with_most_kills = spaceship.sort_impostors_by_kills()[0]
        return impostor_with_most_kills


if __name__ == "__main__":
    print("Spaceship.")

    spaceship = Spaceship()
    print(spaceship.get_dead_players())  # -> []
    print()

    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    white = Crewmate("White", "Impostor")
    yellow = Crewmate("Yellow", "Guardian Angel", tasks=5)
    green = Crewmate("green", "Altruist")
    blue = Crewmate("BLUE", "Sheriff", tasks=0)

    print(red)  # -> Red, role: Crewmate, tasks left: 10.
    print(white)  # -> White, role: Crewmate, tasks left: 10.
    print(yellow)  # -> Yellow, role: Guardian Angel, tasks left: 5.
    print(blue)  # -> Blue, role: Sheriff, tasks left: 0.
    print()

    print("Let's make Yellow complete a task.")
    yellow.complete_task()
    print(yellow)  # ->  Yellow, role: Guardian Angel, tasks left: 4.
    print()

    print("Adding crewmates to Spaceship:")
    spaceship.add_crewmate(red)
    spaceship.add_crewmate(white)
    spaceship.add_crewmate(yellow)
    spaceship.add_crewmate(green)
    print(spaceship.get_crewmate_list())  # -> Red, White, Yellow and Green

    spaceship.add_impostor(blue)  # Blue cannot be an Impostor.
    print(spaceship.get_impostor_list())  # -> []
    spaceship.add_crewmate(blue)
    print()

    print("Now let's add impostors.")
    orange = Impostor("orANge")
    black = Impostor("black")
    purple = Impostor("Purple")
    spaceship.add_impostor(orange)
    spaceship.add_impostor(black)

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    print(spaceship.get_impostor_list())  # -> Orange, Black and Purple
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    spaceship.kill_crewmate(black, "purple")  # You can't kill another Impostor, silly!
    print(spaceship.get_dead_players())  # -> Yellow
    print()

    print("Yellow is a Guardian angel, and can protect their allies when dead.")
    spaceship.protect_crewmate(yellow, green)
    print(green.protected)  # -> True
    spaceship.kill_crewmate(orange, "green")
    print(green in spaceship.dead_players)  # -> False
    print(green.protected)  # -> False
    print()

    print("Green revives their ally.")
    spaceship.kill_crewmate(purple, "RED")
    spaceship.revive_crewmate(green, red)
    print(red in spaceship.dead_players)  # -> False
    print()

    print("Let's check if the sorting and filtering works correctly.")

    red.complete_task()
    print(spaceship.get_role_of_player("Blue"))  # -> Sheriff
    spaceship.kill_crewmate(purple, "blue")
    print(spaceship.sort_crewmates_by_tasks())  # -> Red, White
    print(spaceship.sort_impostors_by_kills())  # -> Purple, Orange, Black
    print(spaceship.get_regular_crewmates())  # -> White, Red

