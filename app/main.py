from fastapi import FastAPI

from app.database import create_table
from app.routes.customers import router as customers_router


app = FastAPI(
    title="Customer API",
    description="API REST para gerenciamento de clientes",
    version="1.0.0",
)


create_table()


@app.get(
    "/",
    tags=["Home"],
    summary="Verificar status da API"
)
def home():
    return {
        "message": "Customer API funcionando!"
    }


app.include_router(
    customers_router,
    prefix="/customers",
    tags=["Customers"]
)