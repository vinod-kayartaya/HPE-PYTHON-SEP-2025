def factorial(num: int) -> int:
    if num < 0:
        raise ValueError('Invalid input for factorial')
    
    f = 1
    for i in range(1, num+1):
        f *= i

    return f


def add_all(*args) -> float:
    nums = [a for a in args if type(a) in (int, float)]
    return sum(nums)