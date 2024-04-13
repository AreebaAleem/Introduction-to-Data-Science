import pandas as pd
data = pd.read_excel('data.xlsx')
print(data)

print("Silcing data")
print (data[0:2]['Job'])

print("Reading data from index 2")
print (data.loc[2,['Name','Job']])

print("Reading data from index 2 and 4")
print (data.loc[[2,4],['Name','Job']])
