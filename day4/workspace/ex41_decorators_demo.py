def box(fn):
    print('box called')
    def wrapper():
        print('+--------------------------+')
        fn()
        print('+--------------------------+')

    return wrapper


@box
def greet():
    print('Hello, there!')
# using @box is equivalnt of passing the underlying function as an argument and
# substituting the whole decorator+function with the return value of the decorator function
# i.e, wrapper, 
# this now is called `greet`

def main():
    # boxed_greet = box(greet)
    # boxed_greet()
    greet()     # you are actually calling the wapper function


if __name__ == '__main__':
    main()