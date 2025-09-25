from mysql.connector import connect, DatabaseError

def get_connection():
    cfg = {
        'host': 'localhost',
        'port': '3306',
        'username': 'root',
        'password': 'Welcome#123',
        'database': 'customersdb'
    }
    return connect(**cfg)

def create_db_table():
    sql = """create table customers(
        id integer primary key auto_increment,
        name varchar(50) not null,
        email varchar(200) not null unique,
        phone varchar(50) not null unique,
        gender varchar(6) check (gender in ('Male', 'Female')),
        city varchar(100)
        )"""

    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            print('DB/table created successfully')
        except DatabaseError as err:
            print(str(err))

def add_new_customer_data():
    print('Enter new customer details: ')
    name =  input('Name         : ')
    gender = input('Gender       : ')
    email = input('Email        : ')
    phone = input('Phone        : ')
    city = input('City         : ')

    with get_connection() as conn:
        cursor = conn.cursor()
        sql = 'insert into customers(name, gender, email, phone, city) values (%s, %s, %s, %s, %s)'
        try:
            cursor.execute(sql, (name, gender, email, phone, city))
            conn.commit()
            print('New customer data saved successfully')
        except DatabaseError as err:
            print("Couldn't add new customer data!")
            print(str(err))
            conn.rollback()


def list_all_customers():
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = 'select id, name, gender, email, phone, city from customers'
        cursor.execute(sql)
        rows = cursor.fetchall()
        print_customers_as_table(rows)

def search_by_id_email_phone():
    id_email_phone = input('Enter id/email/phone to search: ')
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = 'select id, name, gender, email, phone, city from customers where id=%s or email=%s or phone=%s'
        cursor.execute(sql, (id_email_phone, id_email_phone, id_email_phone))
        row = cursor.fetchone()

        if row is None:
            print("No customer data found matching your input!")
            return
        
        print_one_customer(row)
        
def print_one_customer(cust):
    print('-'*50)
    print(f'ID          : {cust[0]}')
    print(f'Name        : {cust[1]}')
    print(f'Email       : {cust[3]}')
    print(f'Phone       : {cust[4]}')
    print(f'City        : {cust[5]}')
    print('-'*50)


def search_by_city_gender():
    city_gender = input('Enter city or gender: ')
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = 'select id, name, gender, email, phone, city from customers where city=%s or gender=%s'
        cursor.execute(sql, (city_gender, city_gender))
        rows = cursor.fetchall()
        print_customers_as_table(rows)


def delete_customer():
    cust_id = input('Enter customer id to delete: ')
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('select * from customers where id=%s', [cust_id])
        cust = cursor.fetchone()
        if not cust:
            print(f'No customer found with id {cust_id}')
            return

        print_one_customer(cust)

        choice = input('Are you sure you want to delete this customer? (yes/no) ')
        if not choice == 'yes':
            print('You cancelled the delete operation')
            return
        
        try:
            cursor.execute('delete from customers where id=%s', [cust_id])
            conn.commit()
            print(f'{cust[1]}\'s record deleted')
        except DatabaseError as err:
            conn.rollback()
            print('There was an error while trying to delete the customer')
            print(str(err))


def print_customers_as_table(customers):

    if len(customers) == 0:
        print('No customers found!')
        return

    print('-' * 107)
    print(f'{'id':4} {'name':25} {'gender':6} {'email':35} {'phone':12} {'city':20}')
    print('-' * 107)
    for c in customers:
        print(f'{c[0]:^4} {c[1]:25} {c[2]:6} {c[3]:35} {c[4]:12} {c[5]:20}')
    print('-' * 107)


def menu():
    print('--- Main Menu ---')
    print('0. Exit')
    print('1. Create database/table')
    print('2. Add new customer data')
    print('3. List all customers')
    print('4. Search by id/email/phone')
    print('5. Search by gender/city')
    print('6. Update customer data')    
    print('7. Delete customer data')
    print()
    try:
        return int(input('Enter your choice: '))
    except ValueError:
        return -1


def main():
    while True:
        choice = menu()

        if choice not in range(0, 8):
            print('Invalid choice. Please try again.')
            continue

        if choice == 0:
            print('Thank you. Have a nice day.')
            exit(0)

        if choice == 1:
            create_db_table()
        elif choice == 2:
            add_new_customer_data()
        elif choice == 3:
            list_all_customers()
        elif choice == 4:
            search_by_id_email_phone()
        elif choice == 5:
            search_by_city_gender()
        elif choice == 6:
            # update customers set name=?, gender=?, email=?, phone=?, city=? where id=?
            pass
        elif choice == 7:
            delete_customer()


if __name__ == '__main__':
    main()
