import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename = 'D:\Python\surrey-street.csv'
data = pd.read_csv(filename)
#6 - Location, 9 - Crime type, 10 - Last outcome category
df = data.iloc[:,[6,9,10]] 
#print(data.shape)
#print(data.info())
#print(data.describe())
#print(df['Last outcome category'].describe())
#print(df['Last outcome category'].unique())
"""print("====================Cases under investigation====================")
print(df[df['Last outcome category'] == 'Under investigation'].count())

print("====================Complete, no suspect====================")
print(df[df['Last outcome category'] == 'Investigation complete; no suspect identified'].count())

print("====================Offender given a caution====================")
print(df[df['Last outcome category'] == 'Offender given a caution'].count())

print("====================Offender given penalty notice====================")
print(df[df['Last outcome category'] == 'Offender given penalty notice'].count())

print("====================Offender given a drugs possession warning====================")
print(df[df['Last outcome category'] == 'Offender given a drugs possession warning'].count())

print("====================Awaiting court outcome====================")
print(df[df['Last outcome category'] == 'Awaiting court outcome'].count())

print("====================Local resolution====================")
print(df[df['Last outcome category'] == 'Local resolution'].count())"""

#print(df['Crime type'].unique())

"""crimes_dict = {'Public order': df[df['Crime type'] == 'Public order'].count().sum(),
			'Burglary': df[df['Crime type'] == 'Burglary'].count(), 
			'Other crime': df[df['Crime type'] == 'Other crime'].count(), 
			'Other theft': df[df['Crime type'] == 'Other theft'].count(), 
			'Robbery': df[df['Crime type'] == 'Robbery'].count(), 
			'Anti-social behaviour': df[df['Crime type'] == 'Anti-social behaviour'].count(), 
			'Criminal damage and arson': df[df['Crime type'] == 'Criminal damage and arson'].count(), 
			'Vehicle crime': df[df['Crime type'] == 'Vehicle crime'].count(), 
			'Shoplifting': df[df['Crime type'] == 'Shoplifting'].count(), 
			'Drugs': df[df['Crime type'] == 'Drugs'].count(), 
			'Bicycle theft': df[df['Crime type'] == 'Bicycle theft'].count(), 
			'Possession of weapons': df[df['Crime type'] == 'Possession of weapons'].count(), 
			'Theft from the person': df[df['Crime type'] == 'Theft from the person'].count()}
plt.bar(crimes_dict.keys(), crimes_dict.values(), color='g')
plt.show()"""
new_df = data[['Location', 'Crime type', 'Last outcome category']]
print(new_df.shape)
print(new_df.loc[new_df.notnull().all(), :]
)
"""
print("Public order")
print(df['Crime type'].str.contains('Public order').sum())
print("Burglary")
print(df['Crime type'].str.contains('Burglary').sum())
print("Other crime")
print(df['Crime type'].str.contains('Other crime').sum())
print("Other theft")
print(df['Crime type'].str.contains('Other theft').sum())
print("Robbery")
print(df['Crime type'].str.contains('Robbery').sum())
print("Anti-social behaviour")
print(df['Crime type'].str.contains('Anti-social behaviour').sum())
print("Criminal damage and arson")
print(df['Crime type'].str.contains('Criminal damage and arson').sum())
print("Vehicle crime")
print(df['Crime type'].str.contains('Vehicle crime').sum())
print("Shoplifting")
print(df['Crime type'].str.contains('Shoplifting').sum())
print("Drugs")
print(df['Crime type'].str.contains('Drugs').sum())
print("Bicycle theft")
print(df['Crime type'].str.contains('Bicycle theft').sum())
print("Possession of weapons")
print(df['Crime type'].str.contains('Possession of weapons').sum())
print("Theft from the person")
print(df['Crime type'].str.contains('Theft from the person').sum())
#df['Location']
#df['Last outcome category']
"""
