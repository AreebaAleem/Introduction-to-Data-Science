#Drop rows with missing values

import pandas as pd

df = pd.read_csv('data_with_missing.csv')
print(df['Salary'].isnull())