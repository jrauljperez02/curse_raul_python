#https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
#in this link you could download csv file for this lesson

import pandas
from pandas.core.tools.datetimes import to_datetime
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
black = 0
gray = 0
red = 0
other = 0
for color in data['Primary Fur Color']:
    if color == 'Black':
        black +=1
    elif color == 'Gray':
        gray += 1
    elif color == 'Cinnamon':
        red += 1
    else:
        other += 1

color_dict = {'color':['Black','Gray','Red','Other'],
              'number':[black,gray,red,other]}
final = pandas.DataFrame(color_dict)
final.to_csv('colors.csv')

#other way to do the same code
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])
gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])

color_dict_2 = {'Primary Fur Color':['Black','Gray','Cinnamon'],
                'Number':[black_squirrels,gray_squirrels,red_squirrels]}
final_2 = pandas.DataFrame(color_dict_2)
final_2.to_csv('colors2.csv')
