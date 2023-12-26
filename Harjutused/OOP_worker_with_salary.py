"""
Loo klassid Job def __init__(self, title, salary): ja Person def __init__(self, name, job=None):.
Loo meetodid assign_job() ning work(). Kus lisad inimesele töökoha, ning paned ta tööle.
Töötamise tulemusena peab inimese rahasumma suurenema palga võrra.
"""


class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary


class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job
        self.money = 0

    def assign_job(self, job):
        self.job = job

    def work(self):
        if self.job:
            self.money = self.job.salary


software_engineer = Job("Software Engineer", 6000)
john = Person("John")
print(john.money)

john.assign_job(software_engineer)

john.work()

print(john.money)
