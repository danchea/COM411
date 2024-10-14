## Task 1
#
# char = (input("Program Started!\nEnter a character: "))
# num = len(char)
# if num == 1:
#     print("The ASCII code for t is:",ord(char),"\nProgram Ended!")

## Task2

code = input("Program Started\nPlease enter an ASCII code")
num = abs(ord(code))
if num <= 126 and num >= 32:
    print(f"the character represented by the ASCII code {code} is {num} \nprogram Ended!")
else:
    print("error, incorrect input")