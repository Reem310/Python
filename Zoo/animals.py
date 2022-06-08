from email.base64mime import header_length


class Animals:
    def __init__(self,name, age, health, happiness):
        self.name=name
        self.age= 0
        self.health=health
        self.happiness=happiness

#a display_info method that shows the animal's name, health, and happiness.
    def display(self):
        print(f"Name:{self.name}, Type:{self.type} Health:{self.health}, Happiness:{self.happiness}")
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

class Frog(Animals):
    def __init__(self,name):
        super().__init__(name, age=0, health=10, happiness=80)
        self.type="Frog"
        self.age=0


class Owl(Animals):
    def __init__(self,name):
        super().__init__(name, age=0, health=40, happiness=10)
        self.type="Owl"

class Tiger(Animals):
    def __init__(self,name):
        super().__init__(name, age=0, health=100, happiness=90)
        self.type="Tiger"
        self.speed=150
        print("Tiger Speed:", self.speed)
        


abd=Frog("abd")
abd.feed().display()

abc=Owl("abc")
abc.feed().display()

aba=Tiger("aba")
aba.feed().display() 





