import numpy as np

# sales = np.array([
#     [10000,12000,15000],
#     [11000,13000,16000],
#     [12000,14000,17000]
# ])
# print(sales)
# # print(np.appendmax(sales))  #min, sum ,avg size mean median var std
# print("sum of rows ",np.sum(sales , axis=0))
# print("sum of columns ",np.sum(sales , axis=1))



# branch_sales = np.array([
#     [10000,12000,14000],
#     [15000,17000,19000],
#     [20000,22000,24000]
# ])
# print("Total sales of brach in all the months ",np.sum(branch_sales,axis=1))
# print("Total sales of month in all the branchs ",np.sum(branch_sales,axis=0))
students= np.array(["s1","s2","s3","s4"])
subjects = np.array(["sub1","sub2","sub3","sub4","sub5"])
student_marks = np.array([
    [25,65,75,36,8],
    [65,82,42,21,5],
    [77,44,36,56,74],
    [74,63,45,63,56],
])
subwisePasscount = []
subwiseFailcount = []
for i in range(0,len(subjects)):
    pcount = 0 
    fcount = 0
    for m in student_marks[:,i]:
        if(m>34):
            pcount=pcount+1
        else:
            fcount=fcount+1
    subwisePasscount.append(pcount)
    subwiseFailcount.append(fcount)
print("subject name | pass count | Fail count")
for i in range(0,len(subjects)):
    print(subjects[i]," | ",subwisePasscount[i]," | ",subwiseFailcount[i])
# print(student_marks[:,0])
# print(student_marks[:,1])
# print(student_marks[:,2 ])
# print(student_marks[:,3])
# print(student_marks[:,4])
# for student in student_marks:
#     r = "pass"
#     for marks in student:
#         if(marks<35):
#             r="fail"
#     passfailarray=np.append(passfailarray,r)
# print(passfailarray)
# print("Total marks of students")
# totalmarks =np.sum(student_marks, axis=1)
#create subject array 
# create array for subject wise total :
# create array for pass and fail 
# print(students)
# print(np.sum(student_marks, axis=1))
# for i in range(0,4):
#     print(students[i]," : ",totalmarks[i])