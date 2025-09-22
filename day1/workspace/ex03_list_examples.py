"""
Demonstrates different features of a list
"""

nums = [10, 20, 30, 55, 30, 44]

print(f'{nums = }')
print(f'{nums[0] = }')
print(f'{nums[1] = }')
print(f'{nums[2] = }')

nums.append(40)
print(f'{nums = }')
nums.insert(0, 33)
print(f'{nums = }')
nums.insert(10000, 88)
print(f'{nums = }')

n = nums.pop() # removes the last element from the list and returns
print(f'{n = }, {nums = }')
n = nums.pop(1) # removes the element at index 1
print(f'{n = }, {nums = }')

x = 30
# remove x if exists in nums
if x in nums:
    nums.remove(x)
print(f'{nums = }')
