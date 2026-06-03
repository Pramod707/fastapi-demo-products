from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from DataBase import engine, session
import db_model


app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
db_model.base.metadata.create_all(bind=engine)


class Products(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# def init_db():
#     db = session()
#     for pr in products:
#         db.add(db_model.Products(**pr.model_dump()))

#     db.commit()
#     count = db.query(db_model.Products).count()

#     print(f"Total products: {count}")


# init_db()


@app.get("/products")
def get_products(db: session = Depends(get_db)):
    products = db.query(db_model.Products).all()
    return products


@app.get("/products/{id}")
def get_product(id: int, db: session = Depends(get_db)):
    # for pr in products:
    #     if pr.id == id:
    #         return pr
    # return "product not found"
    product = db.query(db_model.Products).filter(db_model.Products.id == id).first()
    return product


@app.post("/products")
def post_product(product: Products, db: session = Depends(get_db)):
    # products.append(product)
    db.add(db_model.Products(**product.model_dump()))
    db.commit()
    if product:
        return "product is added"
    return "product is not added"


@app.delete("/products/{id}")
def delete_product(id: int, db: session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         del products[i]
    #         return "product deleted"
    product = db.query(db_model.Products).filter(db_model.Products.id == id).first()
    if product:
        db.delete(product)
        db.commit()
        return "product is deleted"
    else:
        return "product is not deleted"


@app.put("/products/{id}")
def update_product(id: int, product: Products, db: session = Depends(get_db)):
    db_product = db.query(db_model.Products).filter(db_model.Products.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated"
    return "product not found"

    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products[i] = product
    #         return "product updated"
