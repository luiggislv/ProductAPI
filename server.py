from product_api import db, app, controllers

if __name__ == "__main__":
    db.create_all()
    app.run(port=3000, host="localhost")
