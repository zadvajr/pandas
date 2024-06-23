#pandas dataframe

import pandas as pd

data = {
    'calories': [300, 200, 400],
    'durations': [20, 30, 40],
    '%': [5, 3, 2]
}

#loading data into dataframe

df = pd.DataFrame(data)

print(df)

#locate a single row in pandas dataframe as follows
print(df.loc[0])

#locate multiple rows as follows 
print(df.loc[[0, 1]])

#you can also use named indexes in pandas dataframe
df = pd.DataFrame(data, index=[1,2,3])

print(df)