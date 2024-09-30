age = int(input("Enter your age: "))
print(f"your age is {age}")

if age >= 16:
    print("you can play thr lottery")
else:
    print("you cannot play the lottery")  ##if and else and elif

location = input("Enter your location: ").lower()
time = "7:00"

if location == "Southampton":
    print("set alarm for 8:30")
elif location == "IOW":
    print("set alarm for 7:30")
else:
    print(" set alarm for 6:30")

