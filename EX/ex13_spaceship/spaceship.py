"""Spaceship."""


class Crewmate:
    """Crewmate class."""

    def __init__(self, color: str, role: str, tasks: int = 10):
        """Initialize a Crewmate object."""
        self.color = color.title()
        self.role = role.title()
        self.tasks = tasks
        self.roles = ["Crewmate", "Sheriff", "Guardian Angel", "Altruist"]
        self.protected = False

        if self.role not in self.roles:
            self.role = "Crewmate"

    def __repr__(self):
        """Return a string representation of the Crewmate object."""
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        """Complete a task."""
        if self.tasks > 0:
            self.tasks -= 1


class Impostor:
    """Impostor class."""

    def __init__(self, color: str):
        """Initialize an Impostor object."""
        self.color = color.capitalize()
        self.kills = 0

    def __repr__(self):
        """Return a string representation of the Impostor object."""
        return f"Impostor {self.color}, kills: {self.kills}."


class Spaceship:
    """Spaceship class."""

    def __init__(self):
        """Initialize a Spaceship object."""
        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []

    def get_crewmate_list(self):
        """Return a list of all crewmates in the spaceship."""
        return self.crewmate_list

    def get_impostor_list(self):
        """Return a list of all impostors in the spaceship."""
        return self.impostor_list

    def get_dead_players(self):
        """Return a list of all dead players in the spaceship."""
        return self.dead_players

    def add_crewmate(self, crewmate):
        """Add a crewmate to the spaceship."""
        if not isinstance(crewmate, Impostor) and \
                crewmate.color not in [c.color for c in self.crewmate_list] and \
                crewmate.color not in [i.color for i in self.impostor_list]:
            self.crewmate_list.append(crewmate)

    def add_impostor(self, impostor):
        """Add an impostor to the spaceship."""
        if not isinstance(impostor, Crewmate) and \
                impostor.color not in [c.color for c in self.crewmate_list] and \
                impostor.color not in [i.color for i in self.impostor_list] and \
                len(self.impostor_list) < 3:
            self.impostor_list.append(impostor)

    def kill_impostor(self, sheriff: Crewmate, color: str):
        """If the Crewmate is sheriff, and he guesses color correctly, he can kill an impostor."""
        if sheriff.role == "Sheriff" and sheriff in self.crewmate_list:
            for impostor in self.impostor_list:
                if impostor.color == color.title():
                    self.impostor_list.remove(impostor)
                    self.dead_players.append(impostor)
                    break
            else:
                self.dead_players.append(sheriff)
                self.crewmate_list.remove(sheriff)

    def kill_crewmate(self, impostor: Impostor, color: str):
        """If the Impostor in the Spaceship, he can kill crewmate."""
        if impostor in self.impostor_list:
            for crewmate in self.crewmate_list:
                if crewmate.color == color.title():
                    if crewmate.protected:
                        crewmate.protected = False
                    else:
                        self.crewmate_list.remove(crewmate)
                        self.dead_players.append(crewmate)
                        impostor.kills += 1

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        """If the Crewmate is altruist, he can revive a crewmate."""
        if altruist.role == "Altruist" and altruist in self.crewmate_list and dead_crewmate in self.dead_players:
            self.crewmate_list.append(dead_crewmate)
            self.dead_players.remove(dead_crewmate)
            self.dead_players.append(altruist)
            self.crewmate_list.remove(altruist)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        """If the Crewmate is Guardian Angel, he can protect a crewmate, who is alive."""
        if crewmate_to_protect in self.crewmate_list and \
                guardian_angel.role == "Guardian Angel" and guardian_angel in self.dead_players:
            count = 0
            for crewmate in self.crewmate_list:
                if crewmate.protected:
                    count += 1
            if count == 0:
                crewmate_to_protect.protected = True

    def sort_crewmates_by_tasks(self):
        """Sort the crewmates by tasks in ascending order."""
        return sorted(self.crewmate_list, key=lambda x: x.tasks)

    def sort_impostors_by_kills(self):
        """Sort the impostors by kills in descending order."""
        return sorted(self.impostor_list, key=lambda x: x.kills, reverse=True)

    def get_regular_crewmates(self):
        """Return a string of all regular crewmates in the spaceship."""
        regular_crewmates = []
        for crewmate in self.crewmate_list:
            if crewmate.role == "Crewmate":
                regular_crewmates.append(crewmate)
        return regular_crewmates

    def get_role_of_player(self, color: str):
        """Return the role of the player with the given color."""
        for crewmate in self.crewmate_list:
            if crewmate.color == color.title():
                return crewmate.role
        for impostor in self.impostor_list:
            if impostor.color == color.title():
                return "Impostor"

    def get_crewmate_with_most_tasks_done(self):
        """Return the crewmate with the most tasks done."""
        crewmate_with_least_tasks = Spaceship.sort_crewmates_by_tasks(self)[0]
        return crewmate_with_least_tasks

    def get_impostor_with_most_kills(self):
        """Return the impostor with the most kills."""
        impostor_with_most_kills = Spaceship.sort_impostors_by_kills(self)[0]
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
    print()

    print(spaceship.get_dead_players())
    print(spaceship.get_impostor_list())

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    spaceship.kill_impostor(blue, "white")

    print(spaceship.get_dead_players())
    print(spaceship.get_impostor_list())
