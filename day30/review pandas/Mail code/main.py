with open('names.txt') as names:
    names = names.readlines()

for person in names:
    txt = 'Dear Aang,\nYou are invited to my birthday this Saturday.\nHope you can make it!\nRaul'
    x = txt.replace('Aang',person)

    #lets save each letter into a file 
    with open(f'OUTPUT/{person}.txt',mode='w') as letter:
        letter.write(x)