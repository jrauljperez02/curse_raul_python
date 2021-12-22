from gameData import data
from logos import logo,vs
import random
import os

def get_random_account():
    """Get data from a random account"""
    return random.choice(data)

def showData(account):
    """Lets use this function to be able to rprint all my information"""
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"

def check_answer(guess,a_followers,b_followers):
    """Function to ckeck followers against user's guess and returns True if the got
    ir right or false if they got it wrong"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {showData(account_a)}")
        print(vs)
        print(f"Compare B: {showData(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        """Lets validate each data"""
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        result = check_answer(guess,a_follower_count,b_follower_count)
        os.system("clear")
        if result:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()
