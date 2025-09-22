"""
Using `for` and `while` loops with list
"""

nums = []
while True:
    n = int(input('Enter a number (0 to stop): '))
    if n == 0:
        break
    nums.append(n)

print(f'{nums = }')
squares = []
for i in range(len(nums)):  # looping using index
    squares.append(nums[i] ** 2)
print(f'{squares = }')

squares = []
for n in nums:  # looping using an element from the list
    squares.append(n**2)

print(f'{squares = }')
