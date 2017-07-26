# Flask Restful API - Product

### Install Sqlite3

`sudo apt-get install sqlite3 libsqlite3-dev `

### Install Required

```
sudo pip3 install flask
sudo apt-get install python3-flask-sqlalchemy
```

### Run server

`python3 server.py`


### Services

`Create a new Product - POST`
`http://localhost:3000/product/new_product`

`List Product - GET`
`http://localhost:3000/product/list_product`

`List Product filtered by category - GET`
`http://localhost:3000/product/list_filterby/<string:category_filter>`

`Find Product by ID - GET`
`http://localhost:3000/product/list_product/<int:id>`

`Update Product by ID - PUT`
`http://localhost:3000/product/update/<int:id>`

`Delete Product by ID - DELETE`
`http://localhost:3000/product/delete/<int:id>`

### Run Test

`python3 test/test_product_api.py`
