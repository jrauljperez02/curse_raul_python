#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

from os import name


with open('/home/jrauljperez/Desktop/PROGRAMACION/PYTHON/curse/day24/Mail Merge Project Start/Input/Names/invited_names.txt') as names:
    names = names.readlines()
    #print(names)


for person in names:
    txt = 'Dear Aang,\nYou are invited to my birthday this Saturday.\nHope you can make it!\nRaul'
    x = txt.replace('Aang',person)
    #lets save each leter into a file
    with open(f'Mail Merge Project Start/Output/letter for {person}.txt',mode='w') as letter:
        letter.write(x)
    
    
