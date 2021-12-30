#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

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
    
    