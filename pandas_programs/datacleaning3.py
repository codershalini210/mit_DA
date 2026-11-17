import pandas as pd

data = {
    "emp_id": [101, None, 103, 104, 105, 101, None, 102, 107, 108, 103, 109],
    "name": [
        "Amit", "Neha", "Raj", "Priya", "Karan",
        "Amit", "Sneha", "Neha", "Rahul", "Pooja",
        "Raj", "Vikas"
    ],
    "department": [
        "IT", "HR", "Sales", "IT", "Finance",
        "IT", "HR", "HR", "Sales", "IT",
        "Sales", "Finance"
    ],
    "salary": [
        35000, 42000, 30000, 50000, "45000",
        35000, "38000", 42000, 32000, 50000,
        30000, 40000
    ],
    "city": [
        "Ahmedabad", "Mumbai", "Delhi", "Pune", "Surat",
        "Ahmedabad", "Mumbai", "Mumbai", "Delhi", "Pune",
        "Delhi", "Jaipur"
    ]
}

df = pd.DataFrame(data)
df.drop_duplicates(inplace=True,ignore_index=True,keep="last")
print(df)
# first clean data 
# give total no of emps
# avg salary
# max salary
# //department wise max and avg salary
# count of emps coming from  cities