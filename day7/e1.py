#Step 1 
word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)

#create the list with _
display = []
for letter in range (len(chosen_word)):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()
#verificate every letter

for letter in chosen_word:
    if guess == letter:
        display = guess
    else:
        display = "_"
print(display)

