names = ['Vinod', 'Shyam Sundar', 'Naveen KS', 'Ramesh Iyer']
d1 = {name: len(name) for name in names}
print(f'{d1 = }')

nums = [12, 34, 56, 78, 96, 82]
num_squares = {n: n*n for n in nums}
print(f'{num_squares = }')

fruits = {'apple': 129, 'banana': 65, 'melon': 25}
discount = 0.1  # 10% discount rate

discounted_fruits = {k: int((1-discount)*v) 
                     for k,v in fruits.items()}
print(f'{fruits = }')
print(f'{discounted_fruits = }')

discounted_fruits = {k: int((1-discount)*v) if v>50 else v 
                     for k,v in fruits.items()}
print(f'{discounted_fruits = }')

discounted_fruits = {k: int((1-discount)*v) 
                     for k,v in fruits.items()
                     if v>50 }
print(f'{discounted_fruits = }')
