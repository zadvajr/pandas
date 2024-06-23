#reading data from a json file

import pandas as pd

df = pd.read_json('pandas/data.json')

print(df.to_string()) 