import pandas as pd 
emps =pd.DataFrame({
    "name":["a","b","c","d","e","f","g","h"],
    "salary":[25000,32500,65410,36520,45210,85210,98563,21450],
    "age":[25,28,24,26,23,24,21,27],
        "department":["IT","HR","Admin","IT","HR","Admin","IT","HR"]
},index=["i1","i2","i3","i4","i5","i6","i7","i8"])
# print(emps.info())
# print(emps.describe())
# print(emps.shape)
# print(emps.columns)
# print("-------------------")
# print(emps.dtypes)
# print(emps[0:2])
# print(emps.iloc[0:2])
print(emps.loc["i6":"i8"])