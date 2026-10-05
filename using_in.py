students = ["Aman","Raman","John","Maria","Ron"]
# print("Raman" in students)
name = input("Enter your name ")

if(name.capitalize() in students):
    print(f"congratulations {name} you are selected")
else:
    print(f"Sorry {name} you are not selected")