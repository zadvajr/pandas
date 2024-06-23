#cleaning wrong data format

import pandas as pd

df = pd.read_csv('C:/Users/zadvajr/Desktop/data analytics/pandas/data2.csv')

#convert date column to proper format
df['Date'] = pd.to_datetime(df['Date'])

df.dropna(subset=['Date'], inplace=True)

print(df.to_string())