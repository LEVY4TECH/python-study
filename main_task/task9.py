# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****




star=int(input('Enter a number: '))
for i in range(1, star+1):
    print('*' * i)