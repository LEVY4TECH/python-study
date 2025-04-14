correct_pin='2345'
attempts=3

for i in range(1,4):
    pin=input('Enter your pin: ')
    if pin==correct_pin:
        results='Welcome'
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            results=f'Wrong Pin! You have {remaining_attempts} attempts remaining'
        else:
            results='SimCard Blocked!'
    print(results)
            