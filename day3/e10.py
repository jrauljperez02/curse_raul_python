# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combinated_names = name1 + name2
lowercase_names = combinated_names.lower()
t = lowercase_names.count("t")
r = lowercase_names.count("r")
u = lowercase_names.count("u")
e = lowercase_names.count("e")
first_digit = t + r + u + e

l = lowercase_names.count("l")
o = lowercase_names.count("o")
v = lowercase_names.count("v")
e = lowercase_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit)+str(second_digit))

if score < 10 or score >90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Yor score is {score},you are alright together")
else:
    print(f"Your score is {score}")


