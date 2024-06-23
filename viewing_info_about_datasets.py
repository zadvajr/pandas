#viewing information about dataset

import pandas as pd

df = pd.read_csv('C:/Users/zadvajr/Desktop/data analytics/pandas/data.csv')

#viewing head of data
print(df.head()) #you can specify how many head rows you want to print

print(df.head(20))

# you can also check the tail()
print(df.tail(20))

#you can also print information about data set as follows

print(df.info())