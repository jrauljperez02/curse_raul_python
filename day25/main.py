with open('weather_data.csv') as data_file:
    data = data_file.readlines()
print(data)

'''import csv
with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
print(temperatures)
'''
 
#to read a file .csv with pandas
import pandas
'''There are two type of data in Python - Pandas
    We got DataFrame and Series, wich is 1-dimensional and
    2-dimensional
'''
data = pandas.read_csv('weather_data.csv')
print(data) 


#to convert the file into a dict
data_dict = data.to_dict()
print(data_dict)

#to convert a row into a list and find the average of the list
data_list = data['temp'].to_list()
sum_ = 0
for temperature in data_list:
    sum_ += temperature
average = sum_ / (len(data_list))
print(average)
#another way to find the average is
print(sum(data_list) / (len(data_list)))
#another way to find the average is
print(data['temp'].mean())

#find the maxium value of this list
maxi = data['temp'].max()
print(maxi)

#find just a row
print("---------------------------------")
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])
print("---------------------------------")


monday = data[data.day == 'Monday']
monday_farenheit = (monday.temp * (9/5)) + 32
print(monday_farenheit)

#to create a new 
data_dict_2 = {'students':['Any','Raul','Angelea'],
               'scores':[76,89,82]}

data = pandas.DataFrame(data_dict_2)
data.to_html('new_data.html')