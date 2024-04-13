#Drop rows or col with missing values

import pandas as pd

df = pd.read_csv('data_with_missing.csv')
print(f"dataframe after droping rows with missing values \n {df.dropna(axis=0)}")
print(f"dataframe after droping cols with missing values \n {df.dropna(axis=1)}")