#Some Basic Statistics on Data using numpy

import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
age_list = df.loc[:,"Age"]

mean_age = np.mean(age_list)
print (f"mean age is {mean_age}")
#print (f"min age is {min(age_list)}")