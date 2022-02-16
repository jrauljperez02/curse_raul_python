import pandas
from reportlab.pdfgen import canvas

data = pandas.read_csv('Correos.csv')
names = data['Names']

with open('letter.txt') as letter_file:
    letter_content = letter_file.read()

    for name in names:
        new_letter =  letter_content.replace('[Company]',name.strip())  

        #with open(f'OUTPUTS/letter for {name}.txt',mode='w') as letter:
        #    letter.write(new_letter)
        c = canvas.Canvas(f"OUTPUTS/letter for{name}.pdf")
        c.drawString(120,760,new_letter)
        c.save()

