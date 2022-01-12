#LIST COMPREHENSION
numbers = [1,2,3,4,5]
new_list = []


#first way of list comprehension
for n in numbers:
    add_1 = n + 1

    new_list.append(add_1)
print(new_list)


#second way of list comprehension
new_list = [n + 1 for n in numbers]
print(new_list)


name = 'raul'
new_list_name = [letter for letter in name]
print(new_list_name)

#double of a number
new_list = [n*2 for n in range(1,5)]
print(new_list)


#conditionals
names = ['raul','alex','beth','caroline','dave']