def greet(name: str) -> None:
    print(f'Hello {name}. How are you doing today?')

def print_multiplication_table(num, start=1, end=10) -> None:
    for i in range(start, end+1):
        print(f'{num} X {i} = {num*i}')

def doubleit(num: int) -> int:
    return num * 2

# adding a ,/ after the last parameter (i.e, def add(n1, n2, /):...), restricts the usage
# the function may not be called using keyword arguments
# add(10, 20) --> works
# add(n1=100, n2=200) --> error
def add(n1, n2):        
    print(f'Inside add function, {n1=}, {n2=}')
    return n1 + n2;


if __name__ == '__main__':
    print(add(10, 20))
    print(add(5, 6))
    # print(add(55))    # TypeError: add() missing 1 required positional argument: 'n2'
    # print(add(55, 66, 77)) # TypeError: add() takes 2 positional arguments but 3 were given 
    print(add(n1=100, n2=200))
    print(add(n2=76, n1=90))


    greet(100)
    greet('Vinod')
    greet(False)
    greet(None)
    # print_multiplication_table(15)
    print_multiplication_table(15, end=20)
    # print_multiplication_table(15, 11, 20)
    # print_multiplication_table(15, start=11, end=20)
    x = 123
    y = doubleit(x)

    print(f'{x=}, {y=}')
