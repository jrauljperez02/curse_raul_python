PLACEHOLDER = '[name]'

with open('Input/Names/invited_names.txt') as names_files:
    names = names_files.readlines()

with open('Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER,name.strip())
        #now let sae each file with the respective name file

        with open(f'Output/letter for {name}',mode='w') as letter:
            letter.write(new_letter)