#lower case
name=" JOHn ."
name=name.lower()
name=name.replace('.',' ')
name=name.strip()
print(name)

# Slicing. The Dog Breed is German Shepherd to display Breed is German
sentence_one="The Dog Breed is German Shepherd"
print(sentence_one[8:23])

# Slicing. Defeats for the Clinton forces, this was her moment of triumph only display Clinton forces
sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])

# splitting a sentence
my_text="The lazy dog; ran so fast; it hit the wall"
print(my_text.split(';'))
print(len(my_text))

# cleaning first_name
first_name="  Joh.n"
first_name=first_name.replace('.','')
first_name=first_name.strip()

# cleaning last_name
last_name="   Do,e"
last_name=last_name.replace(',','')
last_name=last_name.strip()

#joining the first and last name
full_name=first_name+" "+last_name
print(full_name)

# Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
# r=r[1:12]
r=r.replace(',','').replace('"','').replace('[','').replace(']','')
print(r)




