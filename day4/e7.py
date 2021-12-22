import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("What do you choose? ")
user_choice = int(input("Type 0 for Rock, 1 for paper or 2 for scissors "))
game_images = [rock,paper,scissors]

computer_choice = random.randint(0,2)

if user_choice == 0  and computer_choice == 2:
    print("Your chose")
    print(game_images[user_choice])
    print("Computer chose")
    print(game_images[computer_choice])
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("Your chose")
    print(game_images[user_choice])
    print("Computer chose")
    print(game_images[computer_choice])
    print("You lose")
elif computer_choice > user_choice:
    print("Your chose")
    print(game_images[user_choice])
    print("Computer chose")
    print(game_images[computer_choice])
    print("You lose!")
elif computer_choice > user_choice:
    print("Your chose")
    print(game_images[user_choice])
    print("Computer chose")
    print(game_images[computer_choice])
    print("You lose")
elif computer_choice == user_choice:
    print("Your chose")
    print(game_images[user_choice])
    print("Computer chose")
    print(game_images[computer_choice])
    print("It's a draw")
else:
    print("You type and invalid number, you lose!")
