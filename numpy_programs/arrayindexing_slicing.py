import numpy as np
# sales = np.array([5200,652,3652,9852,6547,1254])
# # print(sales>6000)
# print(sales[sales>6000])
# print(sales[[1,3,5]])
sales = np.array([
    [5000,7000,9000],
    [4000,6000,8000],
    [3000,5000,7000]
])
# print(sales[sales>6000])
print(sales[[0,2],[1,2] ])
print(sales[[0,0],[1,2]])


# student_marks = np.array([25,35,42])
# All_student_marks = np.array([
#     [52,63,42],
#     [55,54,65],
#     [85,78,89],
#     [55,69,78]])
# print(student_marks[0])
# print(All_student_marks[1,0])
# print(All_student_marks[0])
# print(All_student_marks[:,0])
# print(All_student_marks[:,0:2])
# print("--"*10)
# print(All_student_marks[0:2,1:3])