# this code replaces empty values 

import pandas as pd

df = pd.read_csv('C:/Users/zadvajr/Desktop/data analytics/pandas/data.csv')

df.fillna(130, inplace=True)

print(df.to_string())