# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”


# speed=int(input('Enter car speed: '))
# speed_limit=70

# if speed<70:
#     print('Ok')
# else:
#     points=(speed-speed_limit)//5
#     if points>12:
#         print('license Suspended')
#     else:
#         print(f'points is {points}')


def speed_checker(speed):
    speed_limit=70
    if speed<speed_limit:
        return 'Ok'
    else:
        points=(speed-speed_limit)//5
        if points>12:
            return 'License Suspended'
        else:
            return f'Your points is {points}'
        
speed=int(input('Enter car speed: '))
x=speed_checker(speed)
print(x)