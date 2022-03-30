# orderManager

## SETUP
```angular2html
1) Create a virtualenv with python 3.10
2) Activate virtualenv
3) Run sh setup.sh

TO Run Test
    python manage.py test

To Run Server
python manage.py runserver

```
## What includes code
```angular2html
1) User 
    a) Get Token of user
2) Product
    a) Get List of Product
3) Order
    a) Get List of orders by requested User
`   b) Create New order from listed product

```

### AUTH TOKEN

```angular2html
{
  'Authorization': 'Token 0b426964345cd096ec9c8511d05087a06dad1198'
}
```

## API DOCS

```angular2html
1) USER 
    a)
    AUTHREQUIRED:- NO
    URL:- /api-token-auth/
    METHOD:- POST
    PARAMETERS:- {"username": "test_user_1", "password": "Insure12"}
    RESPONSE SAMPLE:- {"token": "0b426964345cd096ec9c8511d05087a06dad1198"}

2) Product
    a) 
    AUTHREQUIRED:- YES
    URL:- /products/
    METHOD:- GET
    PARAMETERS:- {}
    RESPONSE SAMPLE:- {
                        "count": 100,
                        "next": "http://127.0.0.1:8000/products/?limit=10&offset=10",
                        "previous": null,
                        "results": [
                            {
                                "id": 1,
                                "name": "dummy_i",
                                "price": "12.25",
                                "quantity": 56
                            }]

3) Orders
    a)
    AUTHREQUIRED:- YES
    URL:- /orders/
    METHOD:- GET
    PARAMETERS:- {}
    RESPONSE SAMPLE:- {
                        "count": 97,
                        "next": "http://127.0.0.1:8000/orders/?limit=10&offset=10",
                        "previous": null,
                        "results": [
                            {
                                "id": 10,
                                "product": 62,
                                "quantity": 1,
                                "amount_paid": "12.00",
                                "user": 2,
                                "created_at": "2022-03-30T03:12:49.259296Z"
                            }]
    b)
    AUTHREQUIRED:- YES
    URL:- /orders/
    METHOD:- POST
    PARAMETERS:- {"product": 2, "quantity": 12, "amount_paid": 1}
    RESPONSE SAMPLE:- {
                        "id": 1010,
                        "product": 2,
                        "quantity": 12,
                        "amount_paid": "1.00",
                        "user": 2,
                        "created_at": "2022-03-30T05:10:36.501601Z"
                    }
```

### NOTE
```angular2html
Please use postman collection attach for testing
Opply.postman_collection.json
```