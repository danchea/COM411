print("Please enter a word")
user_word = input()
for position in range(0, len(user_word), 2):
    print(user_word[position])
