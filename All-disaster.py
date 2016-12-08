import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pygal
from pygal.style import DarkStyle
from pygal.style import DarkStyle
from pygal.style import DarkStyle

data = pd.read_csv('All-disaster.csv')
# print(data)

#get list conflagration, flood, landslide, storm
disaster = data.DISASTER
injured = data.INJURED
death = data.DEATH
damage = data.DAMAGED
# print(disaster)
# print(injured)
# print(death)

#get list year
year = data.YEAR
list_year = []
for i in year:
    list_year.append(i)
print(list_year)

#get sum injured
sum_injured = 0
for i in injured:
    sum_injured += i

#get sum death
sum_death = 0
for i in death:
    sum_death += i

#get sum damage
sum_damage = 0
for i in damage:
    sum_damage += i

type_disaster = ['Landslide', 'Flood', 'Storm', 'Conflagration']
list_conflagration_injured = []
list_flood_injured = []
list_landslide_injured = []
list_storm_injured = []
list_conflagration_death = []
list_flood_death = []
list_landslide_death = []
list_storm_death = []
list_conflagration_damage = []
list_flood_damage = []
list_landslide_damage = []
list_storm_damage = []
sum_conflagration_injured = 0
sum_conflagration_death = 0
sum_conflagration_damage = 0
sum_flood_injured = 0
sum_flood_death = 0
sum_flood_damage = 0
sum_landslide_injured = 0
sum_landslide_death = 0
sum_landslide_damage = 0
sum_storm_injured = 0
sum_storm_death = 0
sum_storm_damage = 0

for i in range(len(disaster)):
    if disaster[i] == type_disaster[0]:             #get list landslide injured and death
        list_landslide_injured.append(injured[i])
        list_landslide_death.append(death[i])
        list_landslide_damage.append(damage[i])
        sum_landslide_injured += injured[i]
        sum_landslide_death += death[i]
        sum_landslide_damage += damage[i]
    elif disaster[i] == type_disaster[1]:           #get list flood injured and death
        list_flood_injured.append(injured[i])
        list_flood_death.append(death[i])
        list_flood_damage.append(damage[i])
        sum_flood_injured += injured[i]
        sum_flood_death += death[i]
        sum_flood_damage += damage[i]
    elif disaster[i] == type_disaster[2]:           #get list storm injured and death
        list_storm_injured.append(injured[i])
        list_storm_death.append(death[i])
        list_storm_damage.append(damage[i])
        sum_storm_injured += injured[i]
        sum_storm_death += death[i]
        sum_storm_damage += damage[i]
    elif disaster[i] == type_disaster[3]:           #get list conflagration injured and death
        list_conflagration_injured.append(injured[i])
        list_conflagration_death.append(death[i])
        list_conflagration_damage.append(damage[i])
        sum_conflagration_injured += injured[i]
        sum_conflagration_death += death[i]
        sum_conflagration_damage += damage[i]

#calculate to percent landslide, flood, storm, conflagration (injured)
averange_landslide_injured = (sum_landslide_injured/sum_injured)*100
averange_flood_injured = (sum_flood_injured/sum_injured)*100
averange_storm_injured = (sum_storm_injured/sum_injured)*100
averange_conflagration_injured = (sum_conflagration_injured/sum_injured)*100

#calculate to percent landslide, flood, storm, conflagration (death)
averange_landslide_death = (sum_landslide_death/sum_death)*100
averange_flood_death = (sum_flood_death/sum_death)*100
averange_storm_death = (sum_storm_death/sum_death)*100
averange_conflagration_death = (sum_conflagration_death/sum_death)*100
#calculate to percent landslide, flood, storm, conflagration (damage)
averange_landslide_damage = (sum_landslide_damage/sum_damage)*100
averange_flood_damage = (sum_flood_damage/sum_damage)*100
averange_storm_damage = (sum_storm_damage/sum_damage)*100
averange_conflagration_damage = (sum_conflagration_damage/sum_damage)*100

# print(list_landslide_injured)
# print(list_landslide_death)
# print(list_landslide_damage)
# print(list_flood_injured)
# print(list_flood_death)
# print(list_flood_damage)
# print(list_storm_injured)
# print(list_storm_death)
# print(list_storm_damage)
# print(list_conflagration_injured)
# print(list_conflagration_death)
# print(list_conflagration_damage)

pie_chart = pygal.Pie(fill=True, interpolate='cubic', style=DarkStyle)
pie_chart.title = 'All-Disaster Injured'
pie_chart.add('Conflagration', averange_conflagration_injured)
pie_chart.add('Strom', averange_storm_injured)
pie_chart.add('Flood', averange_flood_injured)
pie_chart.add('Landslide', averange_landslide_injured)
pie_chart.render_to_file("All-didsaster Injured.svg")

pie_chart = pygal.Pie(fill=True, interpolate='cubic', style=DarkStyle)
pie_chart.title = 'All-Disaster Death'
pie_chart.add('Conflagration', averange_conflagration_death)
pie_chart.add('Strom', averange_storm_death)
pie_chart.add('Flood', averange_flood_death)
pie_chart.add('Landslide', averange_landslide_death)
pie_chart.render_to_file("All-didsaster Death.svg")

pie_chart = pygal.Pie(fill=True, interpolate='cubic', style=DarkStyle)
pie_chart.title = 'All-Disaster Damage'
pie_chart.add('Conflagration', averange_conflagration_damage)
pie_chart.add('Strom', averange_storm_damage)
pie_chart.add('Flood', averange_flood_damage)
pie_chart.add('Landslide', averange_landslide_damage)
pie_chart.render_to_file("All-didsaster Damage.svg")
