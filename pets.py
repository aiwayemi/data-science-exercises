
class Pet:
    def __init__(self, name, species,age):
        self.name = name
        self.species = species
        self.age = age
        
    def display(self):
        print(f"{self.name} is a {self.species} and {self.name} is {self.age} years old")
        

