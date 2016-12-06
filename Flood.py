import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pygal

data = pd.read_csv('Flood.csv')
print(data)

#get data injured to list
injured = data.INJURED
list_injured = []
for i in injured:
    list_injured.append(i)
print(list_injured)

#get data death to list
death = data.DEATH
list_death = []
for i in death:
    list_death.append(i)
print(list_death)

#get data damaged to list
damage = data.DAMAGED
list_damage = []
for i in damage:
    list_damage.append(i)
print(list_damage)

#get data year to list
year = data.YEAR
list_year = []
for i in year:
    list_year.append(i)
print(list_year)

chart = pygal.Line(title=u'Flood', secondary_range=(0, 605, 55))
chart.x_labels = map(int, list_year)
chart.y_labels = map(int, range(0, 6000, 500))
chart.add('Injured', list_injured)
chart.add('Death', list_death, secondary=True)
chart.render_to_file("Flood.svg")
#Show Graph Chart_XY