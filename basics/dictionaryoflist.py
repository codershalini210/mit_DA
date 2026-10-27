students ={    
    "A":[44,42,55,21],
    "B":[33,22,55,22],
    "C":[44,65,76,39],
    "D":[44,52, 66,43],
    "E":[25,55,65,74]
}
results={}
# print(students)
# print(students["A"])
for sname,marks in students.items():
    aresult ="Pass"
    for m in marks:
        if(m<35):
            aresult="Fail"
            results[sname] = aresult
            break
        results[sname] = aresult
print(results)
# aresult ="Pass"
# for marks in students["C"]:
#     if(marks<35):
#         aresult="Fail"
#         break
# print("A    you are ",aresult)