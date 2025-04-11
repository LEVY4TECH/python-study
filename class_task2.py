students = [
    ["Alice", ["Math", "Physics", "English"]],
    ["Bob", ["Biology", "Chemistry", "History"]],
    ["Charlie", ["Computer Science", "Math", "Art"]]
]
# 1.display english
print(students[0][1][2])
# 2.change charlie to Alex
students[2][0]='Alex'
print(students)
# 3.remove math
students[0][1].pop(0)
students[2][1].pop(1)
print(students)
# 4.insert java before art
students[2][1].insert(1,'java')
print(students)
# 5.insert a  list of another student after  bob  list
students.insert(2,["Levy",["bio","chem","phyc"]])
print(students)