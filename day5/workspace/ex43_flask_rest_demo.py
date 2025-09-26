from flask import Flask, request     # pip install flask

app = Flask(__name__)

customers = [
    dict(id=1, name='Vinod', city='Bangalore', email='vinod@vinod.co', phone='9731424784'),
    dict(id=2, name='Shyam', city='Shivamogga', email='shyam@xmpl.com', phone='9000080000'),
]

@app.get('/api/customers')
def handle_get_all():
    accept_header = request.headers.get('Accept')
    if 'application/json' in accept_header or '*' in accept_header:
        return customers    
    
    return 'The requested media type is not supported', 406


@app.get('/api/customers/<int:cust_id>')
def handle_get_by_id(cust_id):
    result = [c for c in customers if c['id']==cust_id]
    if len(result) == 0:
        return {'message': f'No data found for id {cust_id}'}, 404
    
    return result[0]

@app.post('/api/customers')
def handle_post():
    new_cust = request.get_json()

    # check for unique email
    if 'email' in new_cust:
        if new_cust['email'] in [c['email'] for c in customers]:
            return {'message': 'email already present'}, 400

    # check for unique phone
    if 'phone' in new_cust:
        if new_cust['phone'] in [c['phone'] for c in customers]:
            return {'message': 'phone already present'}, 400

    new_cust['id'] = 1 + max([c['id'] for c in customers])
    customers.append(new_cust)
    return new_cust, 201


@app.route('/')
def index():
    return '<h1>Hello, and welcome to Flask app!<h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)