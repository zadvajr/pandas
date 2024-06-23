#Cleaning empty cells
import pandas as pd

df = pd.read_csv('C:/Users/zadvajr/Desktop/data analytics/pandas/data.csv')

print(df.to_string())

new_df = df.dropna() #this line removes all empty cells in dataset

print(new_df.to_string())