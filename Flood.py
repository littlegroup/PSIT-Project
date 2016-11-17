import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Flood.csv')
#print(data)

#get data year to list
year = data.YEAR
list_year = []
for i in year:
    list_year.append(i)
#print(list_year)

#get data injured to list
injured = data.INJURED
list_injured = []
for i in injured:
    list_injured.append(i)
#print(list_injured)

#get data death to list
death = data.DEATH
list_death = []
for i in death:
    list_death.append(i)
#print(list_death)

x = np.array(list_year)
y1 = np.array(list_death)
y2 = np.array(list_injured)
plt.figure(figsize=(10,10))
plt.bar(x,y1,color='r',width=0.5,label='Death',align='center')
plt.bar(x,y2,color='orange',width=0.5,label='Injured',align='center')
plt.legend(loc=1)
plt.show()
