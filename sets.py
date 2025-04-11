days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

fruits={"banana","orange","apple","mango"}
# type
print(type(fruits))

# add
fruits.add('lemon')
print(fruits)

# remove/delete
# remove, discard
fruits.remove('orange')
print(fruits)

fruits.pop()
print(fruits)

set1={1,2,3,4,5,6,7}
set2={6,7,8,9,10}

set3=set1|set2
set4=set1&set2
set5=set1-set2
set6=set1^set2
print(set3)
print(set4)
print(set5)
print(set6)