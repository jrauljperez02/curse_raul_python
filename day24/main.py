
# #first way of open a file
# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

#second way tp read a file
with open('files/my_file.txt') as file:
    contents = file.read()
    print(contents)

#how to write a file with python but delete everything
with open('/home/jrauljperez/Desktop/PROGRAMACION/PYTHON/curse/day24/files/my_file.txt',mode='w') as file:
    file.write('new text xd') 

#how to write a file and not delete everything
with open('files/my_file.txt',mode='a') as file:
    file.write('\nthis is new text xd')

#this is use to create a completly new file
with open('my_new_file.txt',mode='w') as file:
    file.write('\nthis is new text')