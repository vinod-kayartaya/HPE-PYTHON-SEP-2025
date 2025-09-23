import hello


hello.greet()

print(f'The hello module is created by {hello.AUTHOR_NAME} and can be reached at {hello.AUTHOR_EMAIL}')

for i in range(10):
    hello.welcome()