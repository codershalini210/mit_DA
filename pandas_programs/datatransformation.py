import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Raj"],
    "Marks": [80, 90, 85]
})
# df["Bonus"] = 5
# df["Total"] = df["Marks"]+df["Bonus"]
# print(df)
# df["Marks"]=df["Marks"].apply(lambda x: x+5)
# df["Name_Length"] = df["Name"].apply(len)
# df["Name_Length"] = df["Name"].apply(lambda x : len(x))
# df["Marks"]=df["Marks"].apply(lambda x: x+5 if x>85 else x+2)
df["newMArks"]=df["Marks"].map(lambda x: x+5 if x>85 else x+2)
print(df)
