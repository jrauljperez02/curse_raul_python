import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
another_person = True

bid_dictionary = {}

def find_highest_bidder(biidding_record):
    highest_bid = 0
    for bidder in biidding_record:
        bid_amount =  biidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid =  bid_amount
            winner =  bidder
    print(f"The winner is {winner} and has to pay ${highest_bid}")


while another_person:
    print(logo)
    name = input("Write your name: ")
    bid =  int(input("Type your bid price: "))
    bid_dictionary[name] = bid

    again = input("Type yes if there's another person playing or type no to leave: ")

    if again ==  "yes":
        another_person = True
        os.system("clear")
    elif again == "no":
        os.system("clear")
        another_person = False
        find_highest_bidder(bid_dictionary)

