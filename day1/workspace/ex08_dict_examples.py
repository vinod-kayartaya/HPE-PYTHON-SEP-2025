"""
Example for understanding `dict` (dictionary)
"""

p1 = dict(name='Vinod', age=52, married=True)
p2 = {'name': 'Ravi', 'age': 22, 'city': 'Chennai'}

# access a value using a key
print(p1['name'])
print(p2['city'])

# add new key/value pair
p1['email'] = 'vinod@vinod.co'  # adds a new key/value pair
p2['city'] = 'Mumbai'           # replaces value of an exisiting key

# check if p1 has a key called `email`
if 'email' in p1:
    print(p1['email'])
else:
    print('p1 has no email')

print(f'{p1 = }')
print(f'{p2 = }')

field_names = ['name', 'email', 'phone', 'gender']
p3 = dict.fromkeys(field_names)
p3['email'] = 'vinod@gmail.com'
print(f'{p3 = }')

# existing fields of p3 in p1 will be updated (values are replaced) 
# and addtional fields of p1 (not in p3) will be added to p3
p3.update(p1)

p3.setdefault('empid', 1122)    # added as new key/value since 'empid' does not exist in p3
p3.setdefault('name', 'Vinod Kumar Kayartaya')  # ignored, since 'name' already present as a key
print(f'{p3 = }')


