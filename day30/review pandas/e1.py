file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()


with open('my_file.txt',mode='a') as file:
    file.write('new text')

with open('my_new_file.txt',mode='w') as file:
    file.write('This some some new text')