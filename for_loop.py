x=[10,20,30,40]
for num in x:
    print(num)


# create a list of numbers of 1 to 100
numbers=list(range(1,101))
for i in numbers:
    print(i)
print(numbers)

# display numbers divisible by 5 between 50 and 150

mynumbers=list(range(50,150))
for num in mynumbers:
    if num%5==0:
        print(num)


# store in a list odd numbers from 1 to 50 and stop in 35

odnum=list(range(1,51))
result=[]
for i in odnum:
    if i%2!=0:
        result.append(i)
print(result)
