try:
    a = input('put a numer')
    a += 23
    print(a)
    #dictionary = {'key1':'something first',
    #              'key2':'something second'}
    #error = dictionary['key3']
    #with open('file.txt') as file:
    #    file.readlines()
except FileNotFoundError:
    with open('file.txt',mode='w') as file:
        file.write('hello')
    #raise ValueError('This a error that Raul set')
except KeyError:
    print('There is not thay key')
except TypeError as error:
    raise ValueError(f'{error} set by Raul')
finally:
    print("end")
