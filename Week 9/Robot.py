## Task 1


# class Robot:
#     MAX_ENERGY = 100
#
#     def __init__(self):
#         self.name = "Robot"
#         self.energy = 0
#
#     def display(self):
#         print(f"I am {self.name}")
#
#
# # Test the Robot class
# if __name__ == "__main__":
#     robot = Robot()
#     robot.display()

## Task 2

class Robot:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.energy = 0

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"Robot(name={self.name!r}, energy={self.energy})"

    def __str__(self):
        return f"Robot: {self.name}, Energy: {self.energy}"


# Test the Robot class
if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(repr(robot))
    print(str(robot))