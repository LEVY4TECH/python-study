#introduction to datatypes
f_name="levy"
print(type(f_name))

# indexing and slicing
text="my name is kevin"
print(text[13])
print(text[-3])
print(text[16:10:-1])

#given a string below, extract the following using indexing and slicing

text1="python programming"
#extract python and display

print(text1[0:6])
print(text1[:6])
#extract programming

print(text1[7:18])
print(text1[7:])
#extract the second character

print(text1[1])
#reverse the entire string

print(text1[::-1])

# string methods
my_text="i am a student"
print(my_text.upper())# convert to uppercase
print(my_text.capitalize()) # make the first letter uppercase and the rest lowercase
print(my_text.casefold()) # makes a string not case sensitive
print(my_text.center) # returns a centered string of lenght width
print(my_text.count) # returns the number of non overlapping occurences
print(my_text.encode()) # encord the string using codec registered for coding
print(my_text.endswith)
print(my_text.partition(' ')) # divide the string into three parts using a separator
print(my_text.replace('student','tutor')) #replaces words
print(my_text.isnumeric()) #tells if the nini is a number
print(my_text.title())
print(my_text.endswith('a')) #tells if it ends with that character
print(my_text.split(' ')) #split a string multiple times with a comma
print(my_text.isdecimal()) # checks if its a decimal
print(my_text.isdigit())
print(my_text.join(text1))
print(my_text.strip)
print(my_text.startswith('i'))

