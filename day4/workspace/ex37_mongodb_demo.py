from pymongo import MongoClient

mc = MongoClient('mongodb://localhost:27017/')
db = mc['customersdb']
customers = db['customers']

def add_new_customer():
    print('Enter customer details: ')
    name = input('Name      : ')
    email = input('Email     : ')
    phone = input('Phone     : ')
    c1 = dict(name=name, email=email, phone=phone)

    result = customers.insert_one(c1)
    print(f'New customer saved with id {result.inserted_id}')


def display_all_customers():
    result = customers.find()
    for c in result:
        print(c.get('name'), '-->', c.get('email') )

def main():
    add_new_customer()
    display_all_customers()

if __name__ == '__main__':
    main()
