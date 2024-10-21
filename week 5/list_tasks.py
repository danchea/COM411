# ##Task 1
#
# def directions():
#     steps = []
#     steps.append("Move Forward")
#     steps.append("Move Backward")
#     steps.append("Turn Left")
#     steps.append("Turn Right")
#     print(steps)
#
# def run_task1():
#     directions()


# run_task1()

## Task 2

def movements():
    path = ["forward", 10, "backward", 5 , "left", 3, "right",1]
    return path

def run_task2():
    print("moving...")
    directions = movements()
    print(f"move",directions[0],"for",directions[1],"steps")
    print(f"move", directions[2], "for", directions[3], "steps")
    print(f"move", directions[4], "for", directions[5], "steps")
    print(f"move", directions[6], "for", directions[7], "steps")

run_task2()

