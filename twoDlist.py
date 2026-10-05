Students = ["Aman","John","Ron","Maria","Sam"]
result = []
marks =[
        [65,85,75,63],
        [85,63,45,55],
        [22,36,45,52],
        [63,85,96,75],
        [24,35,21,32]
        ]
for studentmarks in marks:
    r = "Pass"
    for mark in studentmarks:
        if(mark<35):
            r="Fail"
            break
    result.append(r)
print(result)

