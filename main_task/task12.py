# Write a program that prints the largest of 4 inputs taken as input from a user.


def largest_input(inp1,inp2,inp3,inp4):
    if inp1>inp2 and inp1>inp3 and inp1>inp4:
        return f'{inp1} is the largest'
    elif inp2>inp1 and inp2>inp3 and inp2>inp4:
        return f'{inp2} is the largest'
    elif inp3>inp1 and inp3>inp2 and inp3>inp4:
        return f'{inp3} is the largest'
    else:
        return f'{inp4} is the largest'
    
input1=int(input('Enter number1: '))
input2=int(input('Enter number2: '))
input3=int(input('Enter number4: '))
input4=int(input('Enter number5: '))

x=largest_input(input1,input2,input3,input4)
print(x)
    