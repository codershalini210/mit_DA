name  = input("Enter name")
# print("aeiou" in name)
count =0
for ch in name :  
    if(ch in "aeiouAEIOU"):
        count = count+1
print("No of vowels ", count," no of consonents ",(len(name)-count))