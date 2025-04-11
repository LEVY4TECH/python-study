# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.

correct_password='admin@123'
attempts=4

for i in range(1,5):
    password=input('Enter your password: ')
    if password==correct_password:
        print('Access granted')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'wrong password, you have {remaining_attempts} attempts remaining')
        else:
            print('Account Blocked!')