import hello as h


h.greet()

print(f'The hello module is created by {h.AUTHOR_NAME} and can be reached at {h.AUTHOR_EMAIL}')

for i in range(10):
    h.welcome()