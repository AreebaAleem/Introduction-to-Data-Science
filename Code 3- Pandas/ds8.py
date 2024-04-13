#Reading data from specific col

import pandas as pd
df = pd.read_csv('data.csv')
age_list = df.loc[:,"Age"]
print (age_list)