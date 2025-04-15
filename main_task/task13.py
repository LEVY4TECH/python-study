# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.


correct_password='Admin@123'
correct_email='admin@mail.com'
attempts=3

for i in range(1,4):
    password=input('Enter your password: ')
    email=input('Enter your email: ').casefold()
    if password==correct_password and email==correct_email:
        print('Login is Succesful')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'Invalid password or email! You have {remaining_attempts} remaining attempts')
        else:
            print('account blocked!')
    
        
