import random
numbers = [random.randrange(12,65),random.randrange(12,65),random.randrange(12,65),random.randrange(12,65),random.randrange(12,65)]
print(numbers)
# numbers = [23,54,64,34,65,34,77]
# numbers = 

count =0
while count<3:
    i = int(input("Enter no "))
    if(i in numbers):
        print("you won ")
        break
    else:
        if(count<2):
            print("try again")
    count=count+1
if(count==3):
    print("Game over")