def fruits():
    print('inside the function fruits() before returning Apple')
    yield 'Apple'
    print('inside the function fruits() before returning Mango')
    yield 'Mango'
    print('inside the function fruits() before returning Orange')
    yield 'Orange'

def odd_numbers(max):
    for i in range(1, max+1, 2):
        yield i


def main_1():
    for n in odd_numbers(20):
        print(n)

def main():
    print(f'{type(fruits) = }')
    f1 = fruits()
    print(f'{f1 = }')

    print(next(f1))
    print(next(f1))
    print(next(f1))
    print(next(f1))

    # for f in f1:
    #     print(f)

if __name__ == '__main__':
    main()
