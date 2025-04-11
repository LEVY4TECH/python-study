# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
a=56.8926
b=int(a)
print(b)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
c=56.8926
d=round(c,2)
print(d)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
e=56.8926
f=round(e,3)
print(f)

# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float 

g=56.8926
g=str(g)
g=g[3:]
g=g[0]+'.'+g[1:]
g=float(g)
print(g)


# extra teacher's work
# write a program that gets two inputs from the user and then sums them
y=input('enter a number1: ')
z=input('enter a number2: ')
print(type(y))
y=int(y)
print(type(y))
z=int(z)
sum=y+z
print(sum)


