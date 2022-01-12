import random
names = ['carolina','alberto','raul','ana','amtonio','sofia']

new_dict = {name:random.randint(1,100) for name in names if len(name) < 5}

print(new_dict)
