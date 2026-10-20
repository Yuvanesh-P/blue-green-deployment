import os
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Blue-Green Deployment Demo")

APP_VERSION = os.getenv("APP_VERSION", "1.0")
APP_COLOR = os.getenv("APP_COLOR", "Blue")

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Keyboard", "price": 1500},
    {"id": 3, "name": "Mouse", "price": 800}
]

@app.get("/")
def home():
    return {
        "application": "Blue-Green Deployment Demo",
        "version": APP_VERSION,
        "environment": APP_COLOR,
        "message": f"Hello from {APP_COLOR}!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": APP_VERSION,
        "environment": APP_COLOR
    }

@app.get("/info")
def info():
    return {
        "application": "Blue-Green Deployment Demo",
        "version": APP_VERSION,
        "environment": APP_COLOR,
        "apis": ["/", "/health", "/info", "/products", "/products/{product_id}"]
    }

@app.get("/products")
def get_products():
    return {
        "version": APP_VERSION,
        "count": len(PRODUCTS),
        "products": PRODUCTS
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
