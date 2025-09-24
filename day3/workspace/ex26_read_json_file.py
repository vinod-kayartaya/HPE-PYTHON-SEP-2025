import json
from pprint import pprint

def main():
    file = open('customers.json', encoding='utf-8')
    customers = json.load(file)
    print(f'there are {len(customers)} customers')
    print(f'{customers[0] = }')

    print()

    c1 = customers[0]
    pprint(c1)

    print()

    print(f'Name     : {c1['name']}')
    print(f'City     : {c1['city']}')
    print(f'Email    : {c1['email']}')
    print(f'Phone    : {c1['phone']}')

    print('-'*80)

    for c in customers:
        print(c['name'])


if __name__ == '__main__':
    main()
