days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")

# class Task
data = ("Python", "Java", "C++", "JavaScript")
# 1.Print the first and last element.
print(data[0])
print(data[-1])
# 2.Convert the tuple into a list, add "Go", and convert it back.
data=list(data)
print(type(data))
data.append('Go')
print(data)
data=tuple(data)
print(data)
print(type(data))