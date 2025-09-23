def line(ch='-', length=80):
    print(ch*length)


def print_info(**emp):
    # print(f'{type(emp) = }')
    # print(f'{emp = }')
    line(length=30)
    print(f'Name    : {emp.get('name')}')
    print(f'Email   : {emp.get('email', 'not-known')}')
    print(f'Phone   : {emp.get('phone', 'not-known')}')
    print(f'City    : {emp.get('city', 'Bangalore')}')
    line('=', 30)
    

if __name__ == '__main__':
    print_info(name='Vinod', email='vinod@vinod.co', phone='9731424784', city='Bangalore')
    print_info(name='Avinash')