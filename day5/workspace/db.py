from sqlite3 import connect, DatabaseError, Row

def get_connection():
    conn = connect('customersdb.sqlite')
    conn.row_factory = Row
    return conn


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = """create table if not exists customers(
        id integer primary key autoincrement,
        name varchar(50) not null,
        email varchar(200) not null unique,
        phone varchar(50) not null unique,
        city varchar(100)
        )"""
        cursor.execute(sql)
        
def get_all_customers():
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = 'select * from customers'
        cursor.execute(sql)
        customers = cursor.fetchall()
    return customers

def get_customer(cust_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = 'select * from customers where id = ?'
        cursor.execute(sql, [cust_id])
        return cursor.fetchone()
    
def add_customer(customer):
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = 'insert into customers(name, email, phone, city) values (?, ?, ?, ?)'
        try:
            cursor.execute(sql, tuple(customer.values()))
            customer['id'] = cursor.lastrowid
            conn.commit()
            return customer
        except DatabaseError as err:
            conn.rollback()
            raise ValueError(str(err))
        
def delete_customer(cust_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = 'delete from customers where id=?'
        try:
            cursor.execute(sql, [cust_id])
            conn.commit()
        except DatabaseError as err:
            conn.rollback()
            raise ValueError(str(err))
        

def update_customer(cust):
    params = (cust['name'], cust['email'], cust['phone'], cust['city'], cust['id'])
    with get_connection() as conn:
        cursor = conn.cursor()
        sql = 'update customers set name=?, email=?, phone=?, city=? where id=?'
        try:
            cursor.execute(sql, params)
            conn.commit()
        except DatabaseError as err:
            conn.rollback()
            raise ValueError(str(err))
        