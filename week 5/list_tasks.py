# ##Task 1
#
# def directions():
#     steps = []
#     steps.append("Move Forward")
#     steps.append("Move Backward")
#     steps.append("Turn Left")
#     steps.append("Turn Right")
#     return steps
#
# def run_task1():
#     directions()
from xml.sax.saxutils import escape


# run_task1()

## Task 2
#
# def movements():
#     path = ["forward", 10, "backward", 5 , "left", 3, "right",1]
#     return path
#
# def run_task2():
#     print("moving...")
#     directions = movements()
#     print(f"move",directions[0],"for",directions[1],"steps")
#     print(f"move", directions[2], "for", directions[3], "steps")
#     print(f"move", directions[4], "for", directions[5], "steps")
#     print(f"move", directions[6], "for", directions[7], "steps")
#
# run_task2()

## Task 3

# def directions():
#     steps = ["move forward", "move backward", "turn left", "turn right"]
#     return steps
#
# def menu():
#     print("please select a direction")
#     direction = directions()
#     count = 0
#     for d in direction:
#         print(count,":",d)
#         count += 1
# menu()

## Task 4

def directions():
    steps = ["move forward", "move backward", "turn left", "turn right"]
    return steps

def menu_and_outputs():
    count = 0
    direction = directions()
    for d in direction:
        print(count, ":", d)
        count += 1
    destination = int(input("please select a destination"))
    return destination

def run_task4():
    route = []
    print("Working out escape route...")
    for count in range(5):
        menu_and_outputs()
        route.append(steps[destination])
    print(f"escape route:", route)
run_task4()


