import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lenght = len(names)
random_position = random.randint(0,lenght-1)
person_who_will_pay = names[random_position]

print(person_who_will_pay + " is going to buy the meal today! ")
