import smtplib


my_email = 'jraul.jperez71@gmail.com'
my_password = 'Tlaxcala33.'

connection = smtplib.SMTP('stmp.gmail.com')
#to make secure our connection
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email,to_addr='chuchul.cinco@gmail.com',msg='Hello')
connection.close()