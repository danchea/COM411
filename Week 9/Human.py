## Task 1

# class Human:
#     MAX_ENERGY = 100
#     def __init__(self):
#         self.name = "Human"
#         self.age = 0
#         self.energy = Human.MAX_ENERGY
#
#     def display(self):
#         print(f"I am {self.name}")
#
# if __name__ == "__main__":
#     human = Human()
#     human.display()

## Task 2

class Human:
    MAX_ENERGY = 100
    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"Human(name={self.name!r}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"Human: {self.name}, Age: {self.age}, Energy: {self.energy}"

if __name__ == "__main__":
    human = Human()
    human.display()
    print(repr(human))
    print(str(human))

