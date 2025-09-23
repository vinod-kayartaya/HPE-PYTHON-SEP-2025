def find_average(*nums):
    # print(f'{type(nums) = }')
    # print(f'{nums = }')
    return sum(nums) / len(nums)


if __name__ == '__main__':
    a1 = find_average(10, 20, 30, 40)
    a2 = find_average(1, 49, 592, 23, 59, 29, 29, 19, 49, 58, 58)
    a3 = find_average(12)
    print(f'{a1=}')
    print(f'{a2=}')
    print(f'{a3=}')
    