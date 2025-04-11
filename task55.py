# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.

input1=int(input('input1: '))
input2=int(input('input2: '))
input3=int(input('input3: '))

if input1>input2 and input1>input3:
    results=input1 ,'is the largest'
elif input2>input1 and input2>input3:
    results=input2, 'is the largest'
else:
    results=input3, 'is the largest'
print(results)

# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

temp=float(input('temp: '))

if temp>30:
    results='The temperature is too high'
elif temp>15 and temp<=30:
    results='Normal temperature'
else:
    results='Cold temperature'
print(results)


# Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"

c_password='secret123'
inputpass=input('enter password: ')

if inputpass==c_password:
    results='Access granted'
else:
    results='Access denied'
print(results)

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

student_score=int(input('student_score: '))

if student_score>90:
    attendance=int(input('confirm your attendance: '))
    if attendance>80:
        results='Excellent student'
    else:
        results='Good score, but attendance needs improvement'
else:
    results='Apply for retake!'
print(results)

