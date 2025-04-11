# Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?

num=int(input('Enter a number: '))

if num%2==0:
    results='even number'
else:
    results='odd number'

print(results)