n = int(input("Enter any no "))
i=2
while True:
    if(i==n):
           break
    elif(n%i==0):
      print(f"{n} is not prime ")
      break    
    i=i+1
if(n==i):
   print(f"{n} is prime")
   
# i=2
# while(n%i!=0):
#     i=i+1
# if(n==i):
#     print(n," is prime ")
# else:
#     print(n," is not prime")