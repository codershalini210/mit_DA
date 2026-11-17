import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 40000, 60000, 70000, 45000],
    "City":["a","b","c","d","e"]
})
df = df[df["Salary"]>50000]
grouped = df.groupby("Department")["Salary"].count()
print((grouped))