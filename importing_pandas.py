#this is a pandas turotrials
# how to import pandas as pd alias and use dataframe

import pandas as pd

#this is the datasets
mydatasets = {
    "Cars": ["BMW", "Volvo", "Ford"],
    "Passings": [3, 7, 2]
}



myvar = pd.DataFrame(mydatasets)

print(myvar)

#check pandas version
print("Pandas version: ", pd.__version__)