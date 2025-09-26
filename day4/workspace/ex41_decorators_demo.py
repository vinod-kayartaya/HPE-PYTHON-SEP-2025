def box(fn):
    print('box called')
    def wrapper(*args, **kwargs):
        print('+--------------------------+')
        result = fn(*args, **kwargs)
        print('+--------------------------+')
        return result

    return wrapper


@box
def greet():
    print('Hello, there!')
# using @box is equivalnt of passing the underlying function as an argument and
# substituting the whole decorator+function with the return value of the decorator function
# i.e, wrapper, 
# this now is called `greet`

@box
def print_multiplication_table(num, start=1, end=10):
    for i in range(start, end+1):
        print(f'{num} X {i} = {num*i}')

@box
def say_hello(name='friend', city='your city'):
    print(f'Hello {name}. How is weather in {city}?')


def main():
    say_hello()
    say_hello('Vinod')
    say_hello('Shyam', 'Shivamogga')
    # boxed_greet = box(greet)
    # boxed_greet()
    # greet()     # you are actually calling the wapper function
    print_multiplication_table(34, 11, 20)
    print_multiplication_table(start=1, end=5, num=44)

if __name__ == '__main__':
    main()