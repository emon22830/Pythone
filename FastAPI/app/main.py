from fastapi import FastAPI, HTTPException
from .services.products import get_all_products

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome To FastAPI!"}


@app.get("/products")
def get_products():
    return get_all_products()


