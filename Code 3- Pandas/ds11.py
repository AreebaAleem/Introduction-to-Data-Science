#Some Descriptive Statistics on list

import pandas as pd

df = pd.read_csv('data.csv')
age_list = df.loc[:,"Age"]
print(age_list.describe())