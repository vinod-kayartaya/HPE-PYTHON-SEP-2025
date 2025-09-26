from fastapi import FastAPI, HTTPException     # pip install fastapi[all]
import uvicorn
from pydantic import BaseModel


app = FastAPI()

customers = [
    dict(id=1, name='Vinod', city='Bangalore', email='vinod@vinod.co', phone='9731424784'),
    dict(id=2, name='Shyam', city='Shivamogga', email='shyam@xmpl.com', phone='9000080000'),
]

class Customer(BaseModel):
    name: str
    email: str
    phone: str
    city: str = 'Bangalore'


@app.get('/api/customers')
def handle_get_all():
    return customers

@app.get('/api/customers/{cust_id}')
def handle_get_by_id(cust_id: int):
    result = [c for c in customers if c['id']==cust_id]
    if len(result) == 0:
        raise HTTPException(404, f'No data found for id {cust_id}')
    
    return result[0]


@app.post('/api/customers', status_code=201)
def handle_post(new_cust: Customer):

    new_cust = new_cust.model_dump()

    # check for unique email
    if 'email' in new_cust and new_cust['email'] is not None:
        if new_cust['email'] in [c['email'] for c in customers]:
            raise HTTPException(409, 'email already present')

    # check for unique phone
    if 'phone' in new_cust and new_cust['phone'] is not None:
        if new_cust['phone'] in [c['phone'] for c in customers]:
            raise HTTPException(409, 'phone already present')
        
    new_cust['id'] = 1 + max([c['id'] for c in customers])
    customers.append(new_cust)
    return new_cust
    


@app.get('/')
def index():
    return {'message': 'Welcome to FastAPI training'}

if __name__ == '__main__':
    uvicorn.run(app='ex44_fastapi_rest_demo:app', host='0.0.0.0', port=8000, reload=True)