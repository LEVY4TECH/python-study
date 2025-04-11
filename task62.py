# Write a program that displays a numbers 1 to 50 inside a list.

numbers=list(range(1,51))
print(numbers)
# From 1 above display the ones divisible by 7 or 5 inside a list.

numbers=list(range(1,51))
seven=[]
for i in numbers:
    if i%7==0 or i%5==0:
        seven.append(i)
print(seven)

# Find sum and average of values in the range between 10 to 40.

values=list(range(10,41))
total=0
for i in values:
    total+=i
print(total)

# avearge
aver=total/len(values)
print(aver)

# import statistics
# b=statistics.mean(values)
# print(b)


# Put in a list the first 10 odd numbers between 10 to 50. 
odd_numbers=[]
count=0
for num in range(10,51):
    if num%2!=0:
        count+=1
        if count<=10:
            odd_numbers.append(num)
        else:
            break
        print(odd_numbers)
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.

# number=int(input('Enter number: '))
# for i in range(1,11):
#     print(number,'x',i,'=',number*i)

num=int(input('Enter number: '))
for i in range(11):
    mult=num*i
    print(f'{num}*{i}={mult}')
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even_count=0
for i in range(1,51):
    if i%2==0:
        even_count+=1       

print(even_count)


# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.

ls1 = [ ('Jay', 20), ('Mo', 30), ('Mya', 32),('levy',400) ]
total=0
for i in ls1:
    quantity=i[1]
    total+=quantity

print(total)