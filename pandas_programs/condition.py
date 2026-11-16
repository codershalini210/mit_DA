import pandas as pd 
emps =pd.DataFrame({
    "name":["a","b","c","d","e","f","g","h"],
    "salary":[25000,32500,65410,36520,45210,85210,98563,21450],
    "age":[25,28,24,26,23,24,21,27],
        "department":["IT","HR","Admin","IT","HR","Admin","IT","HR"]
})
print(emps[emps["age"]>25])
print("-"*30)
# print((emps["age"]>25) & (emps["department"]=="IT"))
print(emps[(emps["age"]>25) & (emps["department"]=="IT")])

# Q1. Display all employees whose age is greater than 25.
# Q2. Display all employees who belong to the IT department.
# Q3. Display all employees whose salary is greater than ₹40,000.
# Q4. Display all employees who belong to the HR department and have an age less than 26.
# Q5. Display all employees who belong to the IT department OR have a salary greater than ₹80,000.
# Q6. Display all employees whose age is between 23 and 26 (including both).
# Q7. Display all employees who do NOT belong to the Admin department.

# Q8. Display all employees whose salary is greater than ₹30,000 AND age is less than 25.

# Q9. Display all employees who belong to the HR
# or Admin department and have a salary less than ₹50,000.

# Q10. Display all employees whose age is 
# greater than 24 OR salary is
# less than ₹25,000, but exclude employees who belong to the HR department.

# Additional Practice Challenge
# After filtering, try displaying 
# only the name, salary, and department 
# columns instead of the complete DataFrame.