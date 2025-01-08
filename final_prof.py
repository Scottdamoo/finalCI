import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

file_path = r'c:\Users\scott\OneDrive\Documents\YR2_UNIVERSITY\final prof\final.dataset.xlsx'

gdp = pd.read_excel(file_path)
print(gdp.head())  # Display the first 5 rows

#graph 1: my first graph is a time series plot to represent GDP per cpaita for the G7 countries between 1990-2022

plt.figure(figsize=(12, 6))
for country in gdp['Country'].unique():
    country_data = gdp[gdp['Country'] == country]
    plt.plot(country_data['Year'], country_data['GDP'], label=country)


plt.title('GDP per Capita for G7 Countries (1990-2022)')
plt.xlabel('Year')
plt.ylabel('GDP per Capita ($)')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('time_series')
