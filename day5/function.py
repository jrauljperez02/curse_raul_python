import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def easyPassword(nr_letters,nr_symbols,nr_numbers):
    password = ''
    for char in range(nr_letters):
        password += random.choice(letters)
    for symbol in range(nr_symbols):
        password += random.choice(symbols)
    for number in range(nr_numbers):
        password += random.choice(numbers)

    return password

def hardPassword(nr_letters,nr_symbols,nr_numbers):
    pasword = []
    for char in range(nr_letters):
        pasword.append(random.choice(letters))
    for number in range(nr_numbers):
        pasword.append(random.choice(numbers))
    for symbol in range(nr_symbols):
        pasword.append(random.choice(symbols))

    random.shuffle(pasword)
    #concatenate our list
    final_password = ''
    for element in pasword:
        final_password += element

    return final_password
easypass = easyPassword(4,2,3)
hardpass = hardPassword(2,5,4)
print(hardpass)