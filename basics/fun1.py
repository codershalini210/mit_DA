def hello():
    print("hello world how are you today")
    
def welcome(name):   
    print("weclome ",name)
def greetings(name,msg):
    print(msg, "--",name)
# welcome("Aman")
# hello()
# welcome("Raman")
greetings("Ron","Good morning")
greetings(msg="WElCOME",name="Aman")
def calculate(a,b,op):
    result=""
    if(op=="+"):
        result="sum is "+ str(a+b)
    elif(op=="-"):
        result="difference is "+ str(a-b)
    elif(op=="*"):
        result="multiplication is " +str(a*b)
    elif(op=="/"):
        result="division is "+ str(a/b)
    else :
        result= "invalid operator"
    return result 
x=calculate(12,2,'+')
print((x))
print(calculate(op='/',a=50,b=5))
def findmax(nos):
    pass
findmax([98,56,87,33,67])