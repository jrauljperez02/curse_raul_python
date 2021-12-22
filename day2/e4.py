#CALCULATOR BILL
print("Welcome to the tip calculator.")
bill = float(input("What was the bill? "))
p_tip = int(input("What percentaje tip would you like to give? 10,12 or 15? "))
people = int(input("How many people to split the bill? "))
total = bill + ((p_tip/100) *bill)
each = total / people
#each = round(each,2)
each = "{:.2f}".format(each)
print(f"Each person should pay ${each}")