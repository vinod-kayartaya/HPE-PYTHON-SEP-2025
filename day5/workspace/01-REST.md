
SOAP -> Simple Object Access Protocol
-> Inter-operability between applications written in different language/software
-> for example, a client app written in c++ wants to invoke a method in a server app written in Java
-> Standardized by W3C
-> Data is exchanged in XML format
-> client sends a SOAP request using HTTP as carrier
-> server sends a SOAP response as the HTTP response body


REST --> Representational State Transfer
~ Transfer (exchange) of State (data) between a client and a server in different Representations (JSON/XML/CSV etc)

based on 6 constraints
1. client/server
2. stateless
3. layered
4. cacheable
5. Uniform interface
6. code-on-demand (optional)


-> server maintains one ore more resources which are identified by a uniform resource identifier (URI)
    -> http://example.com/api/products
    -> `/products` is a resource, which is a collection of states called `product`
    -> resource is always a plural noun

    -> same resource endpoint represents different operations performed on the state
    -> we use HTTP request methods (GET, POST, PUT, DELETE, PATCH) to perform different CRUD operations
    -> GET -> fetching state
    -> POST -> create a new state in the resource (add a new product to the existing list of products)
    -> PUT/PATCH -> modify the state identified by it's ID
    -> DELETE -> deletes the state from the resource (very rarely)

GET, POST are done on this URI:
http://example.com/api/products

GET, PUT, PATCH, DELETE are performed on this URI:
http://example.com/api/products/{id}

Content negotiation can be achieved using the HTTP request headers.

While asking for (GET, DELETE) a specific type of data, use the ACCEPT header, and while sending (POST/PUT/PATCH) a specific type of data, use the CONTENT-TYPE header

For example,

```
GET /api/products/38
Host: example.com
Accept: application/xml
```

Http status codes:

200 --> OK
201 --> Created
204 --> No content

400 --> Bad request
401 --> Unauthorized
403 --> Forbidden
404 --> Not found
405 --> Method not allowed
406 --> Not acceptable

500 --> Internal server error