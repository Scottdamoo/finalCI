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

#graph 2: my second graph is a box plot to show volatility GDP per capita growth across the G7 countries

plt.figure(figsize=(10, 6))
sns.boxplot(x='Country', y='GDP', data=gdp)
plt.title('Distribution of GDP per Capita for G7 Countries (1990-2022)')
plt.xlabel('Country')
plt.ylabel('GDP per Capita ($)')
plt.xticks(rotation=45)
plt.show()
plt.savefig('box_plot')

#graph 3 and 4: bar chart comparing gdp per captita of G7 countries in 1990 and 2022

bar_1990 = gdp[gdp['Year'] == 1990]
plt.figure(figsize=(10, 6))
plt.bar(bar_1990['Country'], bar_1990['GDP'])
plt.title('GDP per Capita for G7 Countries in 1990')
plt.xlabel('Country')
plt.ylabel('GDP per Capita ($)')
plt.xticks(rotation=45)
plt.show()
plt.savefig('bar_chart1990')

bar_2022 = gdp[gdp['Year'] == 2022]
plt.figure(figsize=(10, 6))
plt.bar(bar_2022['Country'], bar_2022['GDP'])
plt.title('GDP per Capita for G7 Countries in 2022')
plt.xlabel('Country')
plt.ylabel('GDP per Capita ($)')
plt.xticks(rotation=45)
plt.show()
plt.savefig('bar_chart2022')
