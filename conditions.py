age=16

if age>=18:
    print('you are an adult')
else:
    print('you are a minor')


# write a program the checks if a nuber is positive, if it's, print positive, else print negative

number=-5

if number>=0:
    print('positive')
else:
    print('negative')


# write aprogram that asks the user to enter their age. If the age is 18 or above, print Access granted, else print Access denied

# age=input('enter your age: ')
# age=int(age)
# if age>=18:
#     print('Access granted')
# else:
#     print('Access denied')



# # write a program that prints the largest of 4 inputs taken as input from a user
# input1=int(input('enter in1: '))
# input2=int(input('enter in2: '))
# input3=int(input('enter in3: '))
# input4=int(input('enter in4: '))

# if input1>input2 and input1>3 and input1>input4:
#     print(input1, 'is the largest input')
# elif input2>input1 and input2>input3 and input2>input4:
#     print(input2, 'is the largest input')
# elif input3>input1 and input3>input2 and input3>input4:
#     print(input3, 'is the largest input')
# else:
#     print(input4, 'is the largest input')



# password=input('enter password: ')
# correctp='secret123'
# email=input('enter your email: ')
# correcte='admin@gmail.com'

# if password==correctp and email==correcte:
#     print('Access Granted')
# else:
#     print('Access Denied')


# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."



creditscore=input('enter creditscore: ')
creditscore=int(creditscore)
if creditscore>700:
    annualincome=input('enter income: ')
    annualincome=int(annualincome)
    if annualincome>50000:
        print('loan approved')
    else:
        print('income required not met')
else:
    print('credit score too low')