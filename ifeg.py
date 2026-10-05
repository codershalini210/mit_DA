name=input("Enter name ")
age = int(input("Enter age"))
if(age>=60):
    if(age<120):
        print(name," you are a senior citizen")
    else:
        print("invalid age")
else:
    if(age>0):
        print(name," you are not a senior citizen")
    else:
        print("invalid age")
# # take name and salary as input
# give 10% bonus if salary is >50000
# else 20% bonus 
# and show new salary with bonus