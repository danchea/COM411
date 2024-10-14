## Task 3
#
# def listen():
#     sound = input("What sound did you hear?\n")
#     print(f"that was a loud {sound}!")
# listen()

## Task 4
# def identify():
#     view = input("what lies before us?")
#     if view == "a large boulder":
#         print("its time to run")
#     else:
#         print("we'll be fine")
# identify()

## Task 5

# def escape_by(plan):
#     if plan == "jumping over":
#         print("we cannot escape that way! the boulder is too big!")
#     elif plan == "running around":
#         print("we cannot escape that way! the boulder is moving too fast!")
#     elif plan == "cross bridge ahead":
#         print("that might just work! lets go!")
#     else:
#         print("we cannot escape that way! the boulder is in the way")
# escape_by("jumping over")
# escape_by("running around")
# escape_by("cross bridge ahead")

## Task 6

# def cross_bridge (steps):
#     if steps <= 5 and steps >= 0:
#         for i in range(steps):
#             print("Crossed Step")
#         print("We must keep going!")
#     else:
#         for i in range(steps):
#             print("Crossed Step")
#         print("the bridge is collapsing")
# cross_bridge(3)
# cross_bridge(6)

## Task 7

def climb_ladder(remaining,crossed):
    if remaining >= crossed:
        print("still some way to go")
    else:
        print("we are almost there")
climb_ladder(5,2)
climb_ladder(2,5)