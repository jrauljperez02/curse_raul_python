my_email = 'jraul.jperez71@gmail.com'
my_password = 'Tlaxcala33.'

import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.login(user=my_email, password=my_password)
    server.sendmail(from_addr=my_email, to_addr='raul_jimenez_71@yahoo.com', msg='Hello')
    server.starttls()

except:
    print('Something went wrong...')

server.close()