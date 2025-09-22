"""
Demonstrates error handling along with list comprehension
"""

numbers_input = input('Enter a comma separated list of integers: ')
print(f'{numbers_input = }')

nums = numbers_input.split(',')
print(f'{nums = }')

nums = [int(n) for n in nums if n.strip().isnumeric()]
print(f'{nums = }')

sum_of_inputs = sum(nums)
print(f'{sum_of_inputs = }')