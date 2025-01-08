# DAT5902 - final_prof
# Authur: Scott Damoo - ec230088627

# Description

this repository contains the code, analysis, and testing I carried out for the DAT5902 - final project. the final project explores GDP per capita across the Group 7 (G7) nations to ultimately analyse the relationship betweem 'international coopoeration' and 'economic growth'. in asnwering my final hypothesis of “International economic cooperation fosters economic growth“
my analysis includes:

- data loading, load in relevant (cleaned) dataset
- exploratory data analysis, ultimatley used to reveal trends, patterns and anomalies within the dataset through visualisations, such as:
    time-series graph - which allowed me to see long term and short term fluctuations in GDP per capita.
    bar charts - which allowed for the overall changes in GDP per capita across all G7 nations in 1990 and 2022.
    box plots which allowed me to understand the volatility in growth of the GDP per capita growth across the nations.

my findings highlighted key patterns in changes of GDP per capita allowwing me to answer my hypothesis, and compare findings with similar work.

# repository structure:

- 'final.dataset':
    contains the dataset used for my analysis, in the form of an excel file 'final.dataset.xlsx'.

- 'final_prof':
    contains all python code relevant to my analysis
    - 'file_path_: providing a clear path to my used dataset
    - 'gdp': variable name used for my datset
    - 'plt.savefig('time_series')': graph 1 
    - 'plt.savefig('box_plot')': graph 2 
    - 'plt.savefig('bar_chart1990')': graph 3 
    - 'plt.savefig('bar_chart2022')': graph 4 

- 'test.py':
    contains the unit tests for validating my analysis

- 'requirements.txt'
    contains the required libaries in my analysis / unit test

- FIGURES: output visualisations from code, include:
    - 'time_series.png'
    - 'box_plot.png'
    - 'bar_chart2022.png'
    - 'bar_chart1990.png'

- 'README.md'
    repository document (current file)

