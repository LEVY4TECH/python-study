# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

student_score=int(input('Enter student_score: '))
if student_score>90:
    attendance=int(input('attendance: '))
    if attendance>80:
        results='Excellent student'
    else:
        results='Good score, but attendance needs improvement'
else:
    results='Apply for retake!'

print(results)


# so this is where one condition needs to be checked before checking another condition
# if the first condition doesn't meet the minimum requirements, the loop is terminated immediately
# if the first condition is met, the loop now proceeds to check the second condition
# if both conditions are met, a certain judgement is generated
# if only the first condition is met, but the condition is not met, a certain judgement is given

# i think the trick here is to notice hoe the inputs are placed!!
