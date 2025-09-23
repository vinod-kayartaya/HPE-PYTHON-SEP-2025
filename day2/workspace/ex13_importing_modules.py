# from hello import welcome, greet, AUTHOR_EMAIL, AUTHOR_NAME
# from hello import *
from hello import welcome, greet as greeting, AUTHOR_EMAIL, AUTHOR_NAME

print(f'ex13_importing_modules.__name__ is {__name__}')
def say_hello():
    print("Hello, friend")


if __name__ == '__main__':  # this is True when you run this module (not when you import)
    greeting()

    print(f'The hello module is created by {AUTHOR_NAME} and can be reached at {AUTHOR_EMAIL}')

    for i in range(10):
        welcome()
