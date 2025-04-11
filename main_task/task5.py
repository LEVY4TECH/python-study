# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!

input1=int(input('Enter a number: '))
input2=int(input('Enter a number: '))
input3=int(input('Enter a number: '))

if input1>input2 and input1>input3:
    results=input1, 'is the largest'
elif input2>input1 and input2>input3:
    results=input2, 'is the largest'
else :
    results=input3, 'is the largest'

print(results)