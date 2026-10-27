# sno = int(input("Enter startno "))
# eno = int(input("Enter end no "))
# for i in range(sno,eno):  all the even nos between this range
#     print(i,end=" ")

# n = int(input("Enter n "))   #reverse table print
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")
#     if(n*i>50):
#         break

# take no from user and find its prime or not  
n = int(input("Enter any no "))
isPrime = True
for i in range(2,n):
    if(n%i==0):
        isPrime = False
        break
if(isPrime):
    print(n, " is a prime no ")    
else:
    print(n," is not a prime no ")
#find factorial of any no entered by user