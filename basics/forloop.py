students=["Alex","John","Ron","maria"] #list  
# for element in iterable :
#     code 
i=1
for student in students:
    print("student ",i,student)
    i+=1
    if(i==3):
        break
print("--------------------")

# i=0
# while(i<len(students)):
#     # print("student ", (i+1),":",student[i])
#     print(f"student {i+1} : {students[i]}")
#     i=i+1