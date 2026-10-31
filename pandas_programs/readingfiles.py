import pandas as pd 

data = pd.read_csv("./files/customer.csv")
# data = pd.read_excel("./files/sales.xlsx")
# print(data[["Salesperson", "Year"]].head())
# print(data["State"]=="Gujarat")
print(data[data["State"]=="Gujarat"])
# print(data.head())
# print(data.head(2))
# print(data.tail())
# print(data.tail(2))