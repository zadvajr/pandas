#check max_rows in pandas

import pandas as pd

print(pd.options.display.max_rows)

#change max_rows settings

pd.options.display.max_rows = 9999;

print(pd.options.display.max_rows);