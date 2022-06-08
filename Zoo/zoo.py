from animals import Animals
from animals import Owl
from animals import Tiger
from animals import Frog

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_owl(self, name):
        self.animals.append(Owl(name) )
    def add_tiger(self, name):
        self.animals.append(Tiger(name) )
    def add_frog(self, name):
        self.animals.append(Frog(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display()
    def attack(self, attacker, victim):
        self.name=attacker
        self.name=victim

        
zoo1 = Zoo("John's Zoo")
zoo1.add_owl("Nala")
zoo1.add_owl("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_frog("Froggy")
zoo1.print_all_info()