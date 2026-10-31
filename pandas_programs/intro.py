import pandas as pd
# marks = pd.Series([54,62,42,32])
# print(marks)
# print(marks[3])
# print(marks.index)
# print(marks.iloc[2])
# marks = pd.Series([54,62,42,32],index=["Raman","Aman","Ron","John"])

# print(marks)
# print(marks["Aman"])
# print(marks.index)
# marks = marks+5
# print(marks)

# data = pd.DataFrame({
#     "Name":["Aman","Raman","John"],
#     "age":[12,14,16],
#     "marks":[55,36,45]
# })
data = pd.DataFrame({
    "Name":["Aman","Raman","John"],
    "age":[12,14,16],
    "marks":[55,36,45]
},index=["s1","s2","s3"])
print(data)
print(data.loc["s2"])