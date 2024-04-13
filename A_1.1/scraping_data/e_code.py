import pandas as pd
import numpy as np
from textblob import TextBlob

df = pd.read_csv('data.csv')

print(f"Shape of data frame is {df.shape}")
print(f"Rows count is {df.shape[0]}")
print(f"Col count is {df.shape[1]}")


missing_values = df.isnull().sum()
print("Missing Values:")
print(missing_values)

df['Price'].fillna(0, inplace=True)
df.dropna(subset=['Reviews'], inplace=True)

df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').astype(float)


df['Revenue'] = df['Price'] * df['Sold']

filtered_data = df[df['Ratings'] >= 4.0]

sorted_data = df.sort_values(by='Sold', ascending=False)


print(df.info())

print("-----------------------------------------------------------------------------------------------------")

print(df.describe())

print("-----------------------------------------------------------------------------------------------------")

print("PRICE")
price_list = df.loc[:,"Price"]
# print (price_list)
max_price = max(price_list)
print (f"Max Product Price is {max_price}")
print (f"Min Product Price is {min(price_list)}")
mean_price = np.mean(price_list)
print (f"Average Price is {mean_price}")
print(price_list.describe())
print("statistics")
print(np.percentile(df.loc[:,"Price"],0))
print(np.std(df.loc[:,"Price"]))

print("-----------------------------------------------------------------------------------------------------")

print("REVENUE")
revenue_list = df.loc[:,"Revenue"]
max_revenue = max(revenue_list)
print (f"Maximum Revenue is {max_revenue}")
mean_revenue = np.mean(revenue_list)
print (f"Average Revenue is {mean_revenue}")
print(revenue_list.describe())
print("statistics")
print(np.percentile(df.loc[:,"Revenue"],0))
print(np.std(df.loc[:,"Revenue"]))


print (df.fillna(100))


print(df['Price'].isnull())

#replace method
df['Ratings'].replace(3.6, 4.0, inplace=True)

#drop duplicate rows
df = df.drop_duplicates()



df['Sentiment'] = df['Product'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['Subjectivity'] = df['Product'].apply(lambda x: TextBlob(x).sentiment.subjectivity)

print("Cleaned, Manipulated, and Analyzed DataFrame:")
print(df)

df.to_csv("textblob_analyzed_data.csv", index=False)
