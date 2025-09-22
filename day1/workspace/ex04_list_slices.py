"""
Slice operations on list
"""

nums = [1, 21, 3, 14, 19, 28, 18, 10, 485, 37]
print(f'{nums = }')
print(f'{len(nums) = }')

another_nums = [19, 29, 39]

# nums.append(another_nums)
# nums.extend(another_nums)
nums += another_nums
print(f'{nums = }')
print(f'{len(nums) = }')

# access elements from a list using square braces
print(f'{nums[3] = }')  # value at index 3, i.e, 4th element
print(f'{nums[12] = }')  # value at index 12, i.e, 13th element
# print(f'{nums[13] = }')  # error
print(f'{nums[-1] = }')  # value at last index, i.e, 13th element
print(f'{nums[-13] = }')  # value at index 0 index
# print(f'{nums[-14] = }')  # error

# access more than one element at a given index (slice operation)
# nums[start_index : end_index]  # element at end_index will be omitted

print(f'{nums[4:9] = }')  # (9-4=5 elements from index 4)
print(f'{nums[4:] = }')  # (all elements from index 4)
print(f'{nums[:9] = }')  # (all elements up to index 9, exluding 9th index)
print(f'{nums[-5:-1] = }')  # all elements from index -5 up to -2

print(f'{nums[::-1] = }')  # gives elements in reverse order

# all these operations can also be applied on a str
my_name = 'Vinod Kumar'
print(f'{my_name[::-1] = }')  # reverse of 'Vinod Kumar'

filename = '/Users/vinod/Desktop/budget.xlsx'
new_filename = filename[:-4] + 'csv'

print(f'{filename = }\n{new_filename = }')

nopath_filename = filename.split('/')[-1]
print(f'{nopath_filename = }')