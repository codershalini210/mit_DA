students = {
    "A":{"Maths":85,"Physics":55,"Chemistry":75},
    "B":{"Bio":55,"Physics":15,"Chemistry":45},
    "C":{"Maths":95,"Physics":55,"Chemistry":65},
    "D":{"Bio":15,"Physics":55,"Chemistry":52},
    "E":{"Maths":15,"Physics":55,"Chemistry":22},
    "F":{"Maths":15,"Physics":55,"Chemistry":34},
}
mathcount = 0 
pcount = 0
chemcount = 0
for k,v in students.items():
    if (v["Maths"]<35):
        mathcount = mathcount+1
    if (v["Physics"]<35):
            pcount = pcount+1
    if (v["Chemistry"]<35):
            chemcount = chemcount+1
print(f"Maths {mathcount} , physics :{pcount} chemistry:{chemcount}")
            
    
