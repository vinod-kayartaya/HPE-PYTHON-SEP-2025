"""
This example script illustrates the use of `input()` function and using `if-else` statements.

Exit codes:

0 - normal termination
1 - Invalid age (<1) input by the user
2 - Invalid age (>120) input by the user
"""

age = int(input('Enter your age: '))
# print(f'{age = }, {type(age)=}')

if age < 1:
    print('Invalid human age! Must be more than or equals to 1.')
    exit(1)

if age > 120:
    print('Invalid human age! Must be less than or equals to 120.')
    exit(2)

if age >= 18:
    print(f'You are eligible for voting in India, and you must exercise your right to vote!')
else:
    print(f'Hang on for another {18-age} years, and you can/should vote then.')
