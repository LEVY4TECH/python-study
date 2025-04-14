# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!

# input1=int(input('Enter a number: '))
# input2=int(input('Enter a number: '))
# input3=int(input('Enter a number: '))

# if input1>input2 and input1>input3:
#     results=input1, 'is the largest'
# elif input2>input1 and input2>input3:
#     results=input2, 'is the largest'
# else :
#     results=input3, 'is the largest'

# print(results)


def largest_item(item1,item2,item3):
    if item1>item2 and item1>item3:
        results=item1, 'is the largest'
    elif item2>item1 and item2>item3:
        results=item2, 'is the largest'
    else:
        results=item3,'is the largest'
    return results

itm1=int(input('Enter a number1: '))
itm2=int(input('Enter a number2: '))
itm3=int(input('Enter a number3: '))

s=largest_item(itm1,itm2,itm3)
print(s)