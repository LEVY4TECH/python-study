# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

email=input('Enter email: ')
at='@'
dot='.'

if at and dot in email:
    results='valid email'
else:
    results='Invalid email'

print(results)