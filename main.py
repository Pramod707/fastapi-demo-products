from fastapi import FastAPI

from pydantic import BaseModel
from DataBase import engine, session
import db_model


class Products(BaseModel):
    id: int
    name: str
    description: str


products = [
    Products(id=101, name="iPhone 16", description="Apple Smartphone"),
    Products(id=102, name="Galaxy S25", description="Samsung Smartphone"),
    Products(id=103, name="MacBook Pro", description="Apple Laptop"),
    Products(id=104, name="PlayStation 5", description="Gaming Console"),
    Products(id=105, name="AirPods Pro", description="Wireless Earbuds"),
]
app = FastAPI()

db_model.base.metadata.create_all(bind=engine)


# def init_db():
#     db = session()
#     for pr in products:
#         db.add(db_model.Products(**pr.model_dump()))

#     db.commit()
#     count = db.query(db_model.Products).count()

#     print(f"Total products: {count}")


# init_db()


@app.get("/products")
def get_products():
    db = session()
    products = db.query(db_model.Products).all()
    return products


@app.get("/product/{id}")
def get_product(id: int):
    # for pr in products:
    #     if pr.id == id:
    #         return pr
    # return "product not found"
    db = session()
    product = db.query(db_model.Products).filter(db_model.Products.id == id).first()
    return product


@app.post("/product")
def post_product(product: Products):
    products.append(product)
    return "product is added"


@app.delete("/product/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted"
    return "product not found"


@app.put("/product/{id}")
def update_product(id: int, product: Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated"
    return "product not found"
