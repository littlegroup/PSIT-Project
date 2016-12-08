import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pygal
from pygal.style import LightGreenStyle

data = pd.read_csv('Storm.csv')
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

chart = pygal.Line(title=u'Injured & Death', secondary_range=(0, 130, 26), fill=True, interpolate='cubic', style=LightGreenStyle)
chart.x_labels = map(int, list_year)
chart.y_labels = map(int, range(0, 600, 100))
chart.add('Injured', list_injured)
chart.add('Death', list_death, secondary=True)
chart.render_to_file("Storm_Injured & Death.svg")

chart = pygal.Bar(title=u'Damage(Storm)', fill=True, interpolate='cubic', style=LightGreenStyle)
chart.x_labels = map(int, list_year)
chart.y_labels = map(int, range(0, 600, 100))
chart.add('Damage', list_damage)
chart.render_to_file("Storm_Damage.svg")