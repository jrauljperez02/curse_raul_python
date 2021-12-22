import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

def calculator():
    print(logo)

    #create a list
    operations = {"+":add,
                  "-":subtract,
                  "*":multiply,
                  "/":divide}

    x = int(input("Type the first number: "))
    for key in operations:
        print(key)

    restart = True

    while restart:
        operation_symbol = input("Pick an operation: ")
        y = int(input("Type the next number: "))
        #Select an operation to asign a function
        calculation_function = operations[operation_symbol]
        result = calculation_function(x,y)

        print(f"{x} {operation_symbol} {y} = {result}")

        run_again = input(f"Type 'y to continue calculating with {result}, type 'n' to start new calculation or 'exit' to exit: ")

        if run_again == "y":
            x = result
            restart = True
        elif run_again == "n":
            restart = False
            os.system("clear")
            calculator()
        if run_again == "exit":
            restart = False

calculator()
