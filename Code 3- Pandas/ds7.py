#Counting number of Cols and Rows in a data frame
import pandas as pd
df = pd.read_csv('data.csv')
print(f"Shape of data frame is {df.shape}")
print(f"Rows count is {df.shape[0]}")
print(f"Col count is {df.shape[1]}")