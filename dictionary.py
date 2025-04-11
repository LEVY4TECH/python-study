student1={
    'name':'Levy',
    'age':18,
    'grade':90,
    'subject':'math'
}

# accessing values
# key
print(student1['name'])
print(student1['subject'])

# adding value/updating value
student1['name']='Leshan'
student1['profession']='Mtu wa mkono'
print(student1)

# removing entries
# pop method
student1.pop('subject')
print(student1)
# delete
del student1['age']
print(student1)

# clear
# clears everythin in a dictionary


student1={
    'name':'Levy',
    'age':18,
    'grade':90,
    'subject':'math'
}

# .get(key) method
print(student1.get('grade'))
# key() method
print(student1.keys())
# values() method
print(student1.values())
# item() method
print(student1.items())

student1.update({'age':34,'marks':200,'gender':'male'})
print(student1)


