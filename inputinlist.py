marks=[]
while True:
    m = int(input("Enter marks"))
    marks.append(m)
    ch = input(" do you want to continue y/n")
    if(ch!="y"):
        break
print(marks)
while(True):
    print("="*60)
    i = input('''press\n 1 for total marks \n2 for avg marks \n 
    3 for max marks \n 4 for min marks \n5 for count of marks''')
    if(i=="1"):
        print("Total marks ",sum(marks))
    elif(i=="2"):
        print("avg ",sum(marks)/len(marks))
    elif(i=="3"):
        print("max ",max(marks))
    elif(i=="4"):
        print("min ",min(marks))
    elif(i=="5"):
        print("count ",len(marks))
    else:
        break
    print("="*60)
