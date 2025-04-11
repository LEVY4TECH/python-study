def hello():
    print('hello Techcamp')

hello()

# welcome a function called welcome_message() that print "Welcome to Python!"

def welcome_message():
    print('Welcome to Python!')

welcome_message()


# parameters and arguments
# we're using that question of finding the area of a triangle

def area_triangle(base,height):
    area=base*height*0.5
    print(area)

area_triangle(20,50)
area_triangle(30,40)
x=int(input('Enter base: '))
y=int(input('Enter height: '))
area_triangle(x,y)

# create a function area_of_circle (pi=3.14)

def area_of_circle(r,pi=3.14):
    area=pi*r*r
    print(area)

area_of_circle(6)


# namba 2
# function that checks odd or even number

def check_even_odd(number):
    if number%2==0:
        print('even')
    else:
        print('odd')

check_even_odd(100)
num=int(input('enter number: '))
check_even_odd(num)

# number 5
def largest(num1,num2,num3):
    if num1>num2 and num1>num3:
        res=num1, 'is the largest'
    elif num2>num1 and num2>num3:
        res=num2, 'is the largest'
    else:
        res=num3, 'is the largest'
    return res
    
x=largest(100,300,400)
print(x)
numb1=int(input('Enter a number: '))
numb2=int(input('Enter a number: '))
numb3=int(input('Enter a number: '))
s=largest(numb1,numb2,numb3)
print(s)