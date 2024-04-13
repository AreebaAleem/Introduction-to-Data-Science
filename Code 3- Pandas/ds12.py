#Data info and descriptive analysis

import pandas as pd
import numpy as np
df = pd.read_csv('data.csv')
print(df.info())
#print(df.describe())
#print(np.percentile(df.loc[:,"Age"],0))
#print(np.std(df.loc[:,"Age"]))
