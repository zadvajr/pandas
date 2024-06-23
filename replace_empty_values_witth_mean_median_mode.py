# you can also replace empty values with mean, median and mode

import pandas as pd

df = pd.read_csv("C:/Users/zadvajr/Desktop/data analytics/pandas/data.csv")

#calculate mean and saveit in variable x
x = df["Calories"].mean()  #you can change this line to reflect median or mode

#refill with mean x
df["Calories"].fillna(x, inplace=True)
print(df.to_string())