
import random
#the user and computer should each get 2 random cards
user_cards = []
computer_cards = []

score_user = 0
score_computer = 0


for i in range (0,2):
    user_cards.append(random.randint(1,11))
    score_user += user_cards[i]


for i in range (0,2):
    computer_cards.append(random.randint(1,11))
    score_computer += computer_cards[i]

print(f"user: {user_cards}")
print(f"computer: {computer_cards}")
print(f"User = {score_user}")
print(f"Computer = {score_computer}")

#lets determine if there is a blackjack
if score_user == 21:
    print("User has blackjack")
    print("You win")
elif score_computer == 21:
    print("Computer has blackjack")
    print("You lose")

elif score_user < 21:
    if 11 not in user_cards:
        print("User lose")
    elif 11 in user_cards:
        user_cards[user_cards.index(11)] = 1
        for i in len(user_cards):
            score_user += user_cards[i]
        print(f"User current cards {user_cards}")
        if score_user == 21:
            print("User has blackjack")
            print("You win")
        elif score_user > 21:
            print("User lose")
        elif score_user < 21:
            another_card = input("Type 'y/n' to take other card: ")
            if another_card == "y":
                user_cards.append(random.randint(1,11))
