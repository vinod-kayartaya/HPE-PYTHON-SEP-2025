def box(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        length = len(str(result))
        print("-" * (length + 4))
        print(f"| {result} |")
        print("-" * (length + 4))
    return wrapper

@box
def greet():
    return "Hello, Vinod!"

greet()
