from fastapi import FastAPI

from pydantic import BaseModel


class Products(BaseModel):
    id: int
    name: str
    description: str


products = [
    Products(id=1, name="Product 1", description="Description 1"),
    Products(id=2, name="Product 2", description="Description 2"),
    Products(id=3, name="Product 3", description="Description 3"),
]
app = FastAPI()


@app.get("/products")
def get_products():
    return products


@app.get("/product/{id}")
def get_product(id: int):
    for pr in products:
        if pr.id == id:
            return pr
    return "product not found"


@app.post("/product")
def post_product(product: Products):
    products.append(product)
    return "product is added"


@app.delete("/product/{id}")
def delete_product(id: int):
    for pr in products:
        if pr.id == id:
            products.remove(pr)
            return "product is deleted"
    return "product not found"
