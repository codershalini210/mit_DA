import pandas as pd
import numpy as np 
df = pd.DataFrame({
    "Name": [" Amit ", "Neha", "Raj", None],
    "Age": ["25", "30", "28", "22"],
    "Marks": [80, 90, None, 85]
})
df["Age"]= (df["Age"]).astype(int)
# print("avg age ", sum(df["Age"])/len(df["Age"]))

# df["Marks"]=df["Marks"].fillna(0)

# print((df))

a= (np.average(df["Marks"].fillna(0)))
df["Marks"] = df["Marks"].fillna(a)
df["Name"] = df["Name"].str.strip()
df.dropna(axis=0,inplace=True)
print((df))