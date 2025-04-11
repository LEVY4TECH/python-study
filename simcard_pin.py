# take input of pin from the user
# compare it with the correct pin 1234
# if correct print 'welcome'
# esle print simcard blocked after giving the user 3 attemps
# on each wrong attempt, inform the user the number of remaining attempts


correct_pin='5496'
attempts=3
for i in range(1,4):
    pin=input('enter your pin: ')
    if pin==correct_pin:
        print('welcome')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'wrong pin, you have {remaining_attempts} attempts remaining')
        else:
            print('simcard blocked')