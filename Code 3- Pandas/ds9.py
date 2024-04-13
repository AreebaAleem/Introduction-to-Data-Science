#Some Basic Statistics on Data

import pandas as pd
df = pd.read_csv('data.csv')
age_list = df.loc[:,"Age"]

max_age = max(age_list)
print (f"max age is {max_age}")
print (f"min age is {min(age_list)}")