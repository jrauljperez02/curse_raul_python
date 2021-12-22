import random

def game():
    print("Welcome to the number Guessing Game!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    def easy_level():
        print("You are in easy level")
        lucky_number = random.randint(0,101)
        print(f"Lucky number is {lucky_number}")
        lives_easy = 10
        continue_playing = True

        while continue_playing:
            guess = int(input("Make a guess: "))

            if guess != lucky_number:
                lives_easy -= 1
                print(f"You have {lives_easy} attempts ramaining to guess the number")
                if guess < lucky_number:
                    print("Too slow")
                elif guess > lucky_number:
                    print("Too high")
                elif lives_easy == 0:
                    continue_playing = False
                    print("You ran out of lives. You lose")
            elif guess == lucky_number:
                continue_playing = False
                print("You found the number")
                print("Congratulations")

    def hard_level():
        print("You are in hard_level")
        lucky_number = random.randint(0,101)
        print(f"Lucky number is {lucky_number}")
        lives_easy = 5
        continue_playing = True

        while continue_playing:
            guess = int(input("Make a guess: "))

            if guess != lucky_number:
                lives_easy -= 1
                print(f"You have {lives_easy} attempts ramaining to guess the number")
                if guess < lucky_number:
                    print("Too slow")
                elif guess > lucky_number:
                    print("Too high")
                elif lives_easy == 0:
                    continue_playing = False
                    print("You ran out of lives. You lose")
            elif guess == lucky_number:
                continue_playing = False
                print("You found the number")
                print("Congratulations")


    if difficulty == "easy":
        easy_level()
    elif difficulty == "hard":
        hard_level()


while input("Type 'y/n' to play: ") ==  "y":
    game()
