studentNames = ["Arvind","Raj","Aadvik","Arvind"]
studentNames.append("Rurik")

print(studentNames)
studentNames.insert(0,"Virat")

print(studentNames)
studentNames.sort(reverse=True)
print(studentNames)

print(studentNames.count("Arvind"))

print(len(studentNames))
print(studentNames.pop())
print(studentNames)
print(studentNames.clear())