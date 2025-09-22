"""
List comprehension is a technique of creating a new list using an exising list with modifications
"""

cities = ['Bangalore', 'kolkata', 'NEW   DELHI', 'navi      mumBAI', 'old CHENNai', 'HYderaBAD']
print(f'{cities = }')

lowercase_cities = []
for a_city in cities:
    lowercase_cities.append(a_city.lower())

print(f'{lowercase_cities = }')

titlecase_cities = [a_city.title().replace(' ', '') for a_city in cities]
print(f'{titlecase_cities = }')

nums = [12, 38, 81, 2, 48, 18, 41, 49, 55, 22, 20, 49]
squares = [n*n for n in nums]
print(f'{nums = }')
print(f'{squares = }')

odd_nums = [n for n in nums if n%2]
print(f'{odd_nums = }')

even_nums = [n for n in nums if n%2==0]
print(f'{even_nums = }')