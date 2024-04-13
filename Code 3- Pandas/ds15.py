#Drop from dataframe with how = any|all

import pandas as pd

df = pd.read_csv('data_with_some_all_missing.csv')
print(f"dataframe after droping how = any \n {df.dropna(how='any')}")
print(f"dataframe after droping how = all \n {df.dropna(how='all')}")