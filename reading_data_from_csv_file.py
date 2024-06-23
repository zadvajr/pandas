# read data from csv file
import os
import pandas as pd


#loading csv files into dataframe
df = pd.read_csv('pandas/data.csv')

#to print the entire dataframe use to_string() method

print(df.to_string())

print(os.getcwd())
