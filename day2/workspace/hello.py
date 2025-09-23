"""
A sample module to demonstrate various module features

"""
print(f'hello.__name__ is {__name__}')


AUTHOR_NAME = 'Vinod Kumar'
AUTHOR_EMAIL = 'vinod@vinod.co'


def welcome():
    """
    A simple method to welcome the user. Prints a default message on the STDOUT.
    """
    print("Welcome to Python training")


def greet():
    """
    A simple method to greet a user. Prints a default message on the STDOUT.
    """
    print("Hello, and welcome to Python training")

# when this module is imported in any other files, the following
# will not be executed
if __name__ == '__main__':
    # do some execution like tests etc here
    pass