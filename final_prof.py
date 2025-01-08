import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

file_path = r'c:\Users\scott\OneDrive\Documents\YR2_UNIVERSITY\final prof\final.dataset.xlsx'

gdp = pd.read_excel(file_path)
print(gdp.head())  # Display the first 5 rows
