# # Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

# marks=int(input('Enter your marks: '))

# if marks>79:
#     print('A')
# elif marks>=60 and marks<=79:
#     print('B')
# elif marks>49 and marks<=59:
#     print('C')
# elif marks>=40 and marks<=49:
#     print('D')
# else:
#     print('E')

def marks_checker(marks):
    if marks>79:
        return 'A'
    elif marks>=60 and marks<=79:
        return 'B'
    elif marks>49 and marks<=59:
        return 'C'
    elif marks>=40 and marks<=49:
        return 'D'
    else:
        return 'E'
    
marking=int(input('Enter your mark: '))
y=marks_checker(marking)
print(y)


# x=marks_checker(90)
# print(x)

