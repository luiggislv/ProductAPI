from flask import jsonify, request
from product_api import db, app
from product_api.models import Product


@app.route("/product/new_product", methods=["POST"])
def new_product():
    json = request.get_json()
    name = json.get("name")
    description = json.get("description")
    category = json.get("category")
    price = json.get("price")
    new_product = Product()
    new_product.name = name
    new_product.description = description
    new_product.category = category
    new_product.price = price
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"id": new_product.id}), 201

@app.route("/product/list_product", methods=["GET"])
def list_product():
    product = Product.query.order_by(Product.id).all()
    return jsonify({
        "items": [{"id": x.id, "name": x.name, "description": x.description, "category": x.category, "price": x.price} for x in product]
    }), 200

@app.route("/product/list_filterby/<string:category_filter>", methods=["GET"])
def list_filterby(category_filter):
    x = Product.query.filter(Product.category == category_filter).all()
    print(x.toString())
    return jsonify({
        "items": [{"id": x.id, "name": x.name, "description": x.description, "category": x.category, "price": x.price}]
    }), 200

@app.route("/product/list_product/<int:id>/", methods=["GET"])
def get_product(id):
    x = Product.query.get(id)
    return jsonify({
        "item": {"id": x.id, "name": x.name, "description": x.description, "category": x.category, "price": x.price}
    }), 200

@app.route("/product/update/<int:id>", methods = ['PUT'])
def update_product(id):
    x = Product.query.get(id)
    x.name = request.json.get('name', x.name)
    x.description = request.json.get('description', x.description)
    x.category = request.json.get('category', x.category)
    x.price = request.json.get('price', x.price)
    db.session.commit()
    return jsonify({
        "item": {"id": x.id, "name": x.name, "description": x.description, "category": x.category, "price": x.price}
    }), 200

@app.route("/product/delete/<int:id>", methods = ['DELETE'])
def delete_product(id):
    db.session.delete(Product.query.get(id))
    db.session.commit()
    return jsonify( { 'result': True, "Status": 'Product succesfully deleted' } ), 200
