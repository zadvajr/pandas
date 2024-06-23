#objects as series

import pandas as pd

student = {
    "name": "Daniel Zadva Jnr",
    "age": 25,
    "height": 175,
    "color": "dark"
}

student_data = pd.Series(student)

print(student_data)

#pandas series is like a column while dataframe is the whole table