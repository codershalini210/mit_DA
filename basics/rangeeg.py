# nos = list(range(5))
# print(nos)
# employees 
# salary
# high salary emps name
#salsalarary emps salary
#low salary emps name
#low salary emps salary

students=[]
marks=[]
passstudents=[]
passmarks =[]
failstudents=[]
failmarks=[]
ch = "y"
while(ch=="y"):
    name = input("Enter student name ")
    marks_1 =int(input("Enter marks"))
    students.append(name)
    marks.append(marks_1)
    if(marks_1>34):
        passstudents.append(name)
        passmarks.append(marks_1)
        # pass
        # data added in pass list and pass marks
    else:
        failstudents.append(name)
        failmarks.append(marks_1)
        # fail list
    ch = input("Do you want to continue y/n")
# for i in range(5):
#     
# print(students)
print("student , marks ")
for i in range(len(students)):
    print(f"{students[i]}  , {marks[i]}")
    print("_____________________")
print("total student",{len(students)},"Avg marks",sum(marks)/len(marks))
print("Pass student",{len(passstudents)},"Avg marks",sum(passmarks)/len(passmarks))
print("Fail student",{len(failstudents)},"Avg marks",sum(failmarks)/len(failmarks))