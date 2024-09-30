# #Task 1
#
# book = input("enter type of book")
# if book == "adventure":
#     print("i like adventure books!")
# print("finish reading book!")  ##outside of if loop to print no matter the input
#
# ##Task 2
#
# activity = input("enter an activity")
# if activity == "calculate":
#     print("performing calculations")
# else:
#     print("performing activity")
# print("Activity completed!")
#
# #Task 3
#
# direction = input("enter a direction (up, left, down, right)")
# holder = "down"
# if direction == "up":
#     holder = "upwards"
# elif direction == "left":
#     holder = "leftwards"
# elif direction == "right":
#     holder = "rightwards"
# else:
#     print("Invalid direction")
#     exit()
#
# print (f"i am moving {holder}")

##Task 4
# number =  int(input("Enter a whole number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
##Task 5

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("First number is greater than second number")
elif num2 > num1:
    print("Second number is greater than first number")
else:
    print("they are equal")
