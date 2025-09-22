my_name = 'Vinod Kumar'
my_age = 52

print(my_name)

print('My name is', my_name)
print('My name is ' + my_name + ' and I am ' + str(my_age) + ' years old.')
print(f'My name is {my_name} and I am {my_age} years old.')
print(my_name, my_age)
print(f'{my_name=}, {my_age=}')

my_name = my_name.upper()
print(f'{my_name=}, {my_age=}')

print(f'{my_name.capitalize() = }')
print(my_name.center(80, '_'))
print('_.'*40)

weekdays = "Sunday,Monday,Tuesday,Wednessday,Thursday,Friday,Saturday"
print(f'{type(weekdays) = }')
print(weekdays)
weekdays = weekdays.split(',')
print(f'{type(weekdays) = }')
print(weekdays)

my_address = '''TF-1 Elegant Elite
ISRO Layout
Bangalore'''

print(my_address)