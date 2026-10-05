marks = {"Aman":54,"Ron":22,"John":65,"Maria":52,"sam":24}
passdict={}
faildict={}
for k,v in marks.items():
    if(v>34):
        passdict[k]=v
    else:
        faildict[k] =v
print("Total no of pass students ",len(passdict),"Pass dict ",passdict)
print("Total no of Fail students ",len(faildict),"fail dict",faildict)
# passlist =[]
# faillist =[]
# for k,v in marks.items():
#     if(v>34):
#         passlist.append(k)
#     else:
#         faillist.append(k)
# print("Pass list ",passlist)
# print("fail list",faillist)