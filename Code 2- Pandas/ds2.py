import pandas as pd
data = {'Name':[
        'ali', 'alia', 'sair'
        ],
        'Age':[
            83,30,19
        ]}
df = pd.DataFrame(data, index=['cui_idx1','cui_idx202','cui_idx562'])
print (df)