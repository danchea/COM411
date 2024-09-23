import math
print("please enter your name")
name = input()
print("please enter your age")
age = int(input())
print("please enter your weight(kg)")
weight = int(input())
print("please enter your height(M)")
height = float(input())
calculations = math.ceil((weight/(height*height))) # math.ceil is used to round to 2 S.F.
print(f"{name} you are {age} years old and your bmi is {calculations} ")
