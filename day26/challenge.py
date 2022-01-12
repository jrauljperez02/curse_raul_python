from unicodedata import name


names = ['carolina','alberto','raul','ana','amtonio','sofia']
names = [name.upper() for name in names if len(name) > 5]
print(names)



numbers = [1,2,3,4,5,6]
numbers =  [number**2 for number in numbers]
even = [number for number in numbers if number % 2 == 0]
print(numbers)
print(even)