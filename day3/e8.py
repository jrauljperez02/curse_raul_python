print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rolercoaster!")
    age = int(input("What is your age? "))
    if age<12:
        bill = 5
        print("Child tickets are $5.")
    elif age<=18:
        bill = 7
        print("Youth tickets are $7.")
    elif age>=45 and age<=55:
        print("Everything is going to be okay. Have a free ride on us! ")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a taken photo? Y or N. ")
    if wants_photo == "Y":
        #Add 3 to their bill
        bill = bill + 3
        print(f"Your bill is {bill}")
    elif wants_photo == "N":
        print(f"Your bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride")
