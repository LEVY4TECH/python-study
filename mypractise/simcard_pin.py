# take input of pin from the user
# compare it with the correct pin 1234
# if correct print 'welcome'
# esle print simcard blocked after giving the user 3 attemps
# on each wrong attempt, inform the user the number of remaining attempts


correct_pin='1234'
attempts=3

for i in range(1,4):
    pin=input('Enter your pin: ')
    if pin==correct_pin:
        print('Welcome')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'Wrong pin! You have {remaining_attempts} remaining attempts')
        else:
            print('Blocked! Get PUK')