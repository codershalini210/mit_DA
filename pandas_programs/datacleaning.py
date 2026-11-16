import pandas as pd 
da = pd.read_excel("./files/pandas_data_cleaning_practice.xlsx")
# print(da.isnull())
# da.dropna(inplace=True,axis=1)
da.fillna("None",inplace=True)
print(da.isnull())
da.dropna(inplace=True,axis=1)
print(da.isnull())