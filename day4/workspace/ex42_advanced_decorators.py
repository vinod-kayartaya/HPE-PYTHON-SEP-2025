import time
from datetime import datetime


# decorator for checking method execution time
def check_exec_time(log_to):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = fn(*args, **kwargs)
            end_time = time.time()
            msg = f'time taken to run the function {fn.__name__} = {end_time-start_time:.6f} seconds'
            if log_to.upper() == 'STDOUT':
                print(msg)
            else:
                with open(log_to, 'at', encoding='utf-8') as file:
                    file.write(f'{datetime.now()}: {msg}\n')
            return result
        return wrapper
    return decorator

@check_exec_time(log_to='performance.log')
def is_prime(num: int) -> bool:
    if num < 0:
        return False

    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True


@check_exec_time(log_to='stdout')
def prime_numbers_between(start=1, end=10):
    primes = []
    for i in range(start, end+1):
        if is_prime(i):
            primes.append(i)

    return primes


def main():
    s = int(input('Start    : '))
    e = int(input('End      : '))
    primes = prime_numbers_between(s, e)
    print(f'{primes = }')


if __name__ == '__main__':
    main()
