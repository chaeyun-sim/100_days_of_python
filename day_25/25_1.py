import pandas

data = pandas.read_csv('./day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey = data[data["Primary Fur Color"] == "Gray"]
grey_result = len(grey)
red = data[data["Primary Fur Color"] == "Cinammon"]
red_result = len(red)
black = data[data["Primary Fur Color"] == "Black"]
black_result = len(black)

di = {}
di['Fur Color'] = ['grey', 'cinnamon', 'black']
di['Count'] = [grey_result, red_result, black_result]

didata = pandas.DataFrame(di)
didata.to_csv('new_color_data.csv')