from fastapi import FastAPI
from database import session, engine
import schema_models
from models import Product  # Pydantic schema

app = FastAPI()

# Create tables
schema_models.Base.metadata.create_all(bind=engine)


@app.get('/')
def go():
    return "let go ben"


# ✅ Seed database (NO id)
def init_db():
    db = session()

    products = [
        {"name": "Soda", "description": "Refreshing drink", "price": 1.99, "quantity": 100},
        {"name": "Chips", "description": "Crunchy chips", "price": 2.49, "quantity": 75},
    ]

    for product in products:
        db.add(schema_models.Product(**product))

    db.commit()   # ✅ FIXED
    db.close()

init_db()


# ✅ GET all from DB
@app.get('/products')
def get_products():
    db = session()
    data = db.query(schema_models.Product).all()
    db.close()
    return data


# ✅ GET by ID from DB
@app.get('/products/{id}')
def get_product_by_id(id: int):
    db = session()
    product = db.query(schema_models.Product).filter(schema_models.Product.id == id).first()
    db.close()

    if not product:
        return {"error": "no product found"}

    return product


# ✅ POST to DB (no manual id)
@app.post("/product")
def add_product(product: Product):
    db = session()

    db_product = schema_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    db.close()

    return db_product