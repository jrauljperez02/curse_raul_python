#File not found
try:
    file = open('my_file.txt')
    a_dictionary = {'key':'value'}
    print(a_dictionary['key'])
except FileNotFoundError:
    file = open('my_file.txt','w')
    file.write('This is a test of exceptions')
except KeyError as error_message:
    print(f'The key {error_message} does not exist')
else:
    content = file.read()
    print(content)
finally:
    raise TypeError('This is an error that I made up.')
    