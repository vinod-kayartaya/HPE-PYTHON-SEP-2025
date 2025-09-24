# in functional programming, a function is treated as first-class citizen
# you can pass function as a method argument
# you can return a function from another function
from functools import reduce


def square(n):
    print(f'square() called with {n}')
    return n*n

sqr = lambda n: n*n

def main():
    nums = [19, 28, 37, 46, 55, 44, 33, 22, 11, 66, 77, 88, 99]
    # squares = [ n*n for n in nums ]
    # squares = list(map(square, nums))
    # squares = list(map(sqr, nums))
    squares = list(map(lambda n: n*n, nums))
    print(f'{squares = }')

    names = ['vinod', 'shyam', 'harish', 'manish']
    names_uc = list(map(str.upper, names))
    print(f'{names_uc = }')
    names_len = list(map(len, names))
    print(f'{names_len = }')

    even_nums = [n for n in nums if n%2==0]
    print(f'{even_nums = }')
    odd_nums = list(filter(lambda n: n%2, nums))
    print(f'{odd_nums = }')
    nums_lt_50 = list(filter(lambda n: n<50, nums))
    print(f'{nums_lt_50 = }')


    total = sum(nums)
    largest = max(nums)
    print(f'{total = }')
    print(f'{largest = }')

    # rf = lambda x,y: x+y
    def rf(x, y):
        print(f'{x=}, {y=}')
        return x+y
    
    total = reduce(rf, nums)
    print(f'{total = }')

    # rf = lambda a,b: a if a<b else b
    print(f'{nums=}')
    def rf(a, b):
        print(f'{a=}, {b=}')
        return a if a<b else b
    smallest = reduce(rf, nums)
    
    # smallest = reduce(lambda a,b: a if a<b else b, nums)
    print(f'{smallest = }')
    

if __name__ == '__main__':
    main()
