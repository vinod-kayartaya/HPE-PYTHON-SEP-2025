from fastapi import FastAPI, HTTPException     # pip install fastapi[all]
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from db import init_db, get_all_customers, get_customer, add_customer, delete_customer, update_customer

app = FastAPI()

app.add_middleware(CORSMiddleware, 
    allow_origins=["http://127.0.0.1:5500", 'http://localhost:5500', 'http://192.168.1.75:5500'],
    allow_methods=['*'],
    allow_headers=['*'])

@app.on_event('startup')
def startup_event():
    init_db()


class Customer(BaseModel):
    name: str
    email: str
    phone: str
    city: str = 'Bangalore'


@app.get('/api/customers')
def handle_get_all():
    return get_all_customers()


@app.get('/api/customers/{cust_id}')
def handle_get_by_id(cust_id: int):
    customer = get_customer(cust_id)
    if customer:
        return customer
        
    raise HTTPException(404, f'No data found for id {cust_id}')

@app.post('/api/customers', status_code=201)
def handle_post(new_cust: Customer):
    new_cust = new_cust.model_dump()
    try:
        return add_customer(new_cust)
    except ValueError as err:
        raise HTTPException(409, str(err))


@app.delete('/api/customers/{cust_id}', status_code=204)
def handle_delete(cust_id: int):
    customer = get_customer(cust_id)
    if customer is None:
        raise HTTPException(404, f'No customer found with id {cust_id}')
    
    try:
        delete_customer(cust_id)
    except ValueError as err:
        raise HTTPException(500, str(err))
    

@app.put('/api/customers/{cust_id}')
def handle_post(cust_id: int, customer: Customer):
    customer = customer.model_dump()
    customer['id'] = cust_id
    try:
        update_customer(customer)
        return customer
    except ValueError as err:
        raise HTTPException(400, str(err))


@app.get('/')
def index():
    return {'message': 'Welcome to FastAPI training'}

if __name__ == '__main__':
    uvicorn.run(app='ex45_fastapi_sqlite_rest_demo:app', host='0.0.0.0', port=8000, reload=True)