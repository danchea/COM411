
print("please enter the number of lives")
lives = int(input())
print("please enter your energy level")
energy = int(input())
print("please enter your shield level")
shield = int(input())
heart = ("♥" * lives)
diamond1=("♦" * energy)
diamond2 = ("♦" * shield)
print(f"lives : {heart} \nEnergy: {diamond1} \nShield: {diamond2}")
