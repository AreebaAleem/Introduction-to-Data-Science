#Drop rows with missing values

import pandas as pd

df = pd.read_csv('data_with_missing.csv')

print (df.fillna(100))
#try what replace method does
#how we can drop duplicate rows?