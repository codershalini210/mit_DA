import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Raj", "Sara","Aman","Ron","John"],
    "Marks": [98, 90, 85, 88,25,32,14],
    "Age": [20, 22, 21, 23,21,20,19]
},index=[102,105,101,103,106,104,107])
# df.sort_values(by="Marks",inplace=True,ascending=False)
df.sort_index(inplace=True)
# print(df)
# print(df[(df["Age"]>20) & (df["Marks"]>34)])
print(df[((df["Age"]>20) & (df["Marks"]>34)) | (df["Marks"]>90)])