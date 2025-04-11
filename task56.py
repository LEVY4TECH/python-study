# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."


accounttype=input('Enter acc type: ')
transactionamount=int(input('Enter amount: '))

if accounttype=='standard':
    if transactionamount>500:
        results='Transaction exceeds the limit for Standard accounts.'
    else:
        results='Transaction approved.'
else:
    if transactionamount>1000:
        results='Transaction exceeds the limit for Premium accounts'
    else:
        results='Transaction approved.'
print(results)
