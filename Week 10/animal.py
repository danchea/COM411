class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.energy = 50
        self.hunger = 50

    def run(self, distance):
        if self.energy - distance >= 0:
            self.energy -= distance
            return True
        return False

    def eat(self, amount):
        if self.hunger + amount <= 100:
            self.hunger += amount
            return True
        return False