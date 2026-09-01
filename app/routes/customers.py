import sqlite3

from fastapi import APIRouter, HTTPException, status

from app.database import get_connection
from app.schemas.customer import CustomerCreate, CustomerResponse, CustomerUpdate


router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CustomerResponse,
    summary="Criar cliente",
    description="Cria um novo cliente no banco de dados."
)
def create_customer(customer: CustomerCreate):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO customers (name, email, phone)
            VALUES (?, ?, ?)
            """,
            (
                customer.name,
                customer.email,
                customer.phone
            )
        )

        connection.commit()

        customer_id = cursor.lastrowid

        return {
            "id": customer_id,
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone
        }

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="E-mail já cadastrado"
        )

    finally:
        connection.close()


@router.get(
    "/",
    response_model=list[CustomerResponse],
    summary="Listar clientes",
    description="Retorna todos os clientes cadastrados."
)
def list_customers(search: str | None = None):
    connection = get_connection()

    if search:
        customers = connection.execute(
            """
            SELECT *
            FROM customers
            WHERE name LIKE ? OR email LIKE ?
            """,
            (
                f"%{search}%",
                f"%{search}%"
            )
        ).fetchall()

    else:
        customers = connection.execute(
            "SELECT * FROM customers"
        ).fetchall()

    connection.close()

    return [dict(customer) for customer in customers]


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
    summary="Buscar cliente",
    description="Busca um cliente pelo seu ID."
)
def get_customer(customer_id: int):
    connection = get_connection()

    customer = connection.execute(
        """
        SELECT *
        FROM customers
        WHERE id = ?
        """,
        (customer_id,)
    ).fetchone()

    connection.close()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return dict(customer)


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
    summary="Atualizar cliente",
    description="Atualiza os dados de um cliente existente."
)
def update_customer(
    customer_id: int,
    customer: CustomerUpdate
):
    connection = get_connection()

    existing_customer = connection.execute(
        """
        SELECT *
        FROM customers
        WHERE id = ?
        """,
        (customer_id,)
    ).fetchone()

    if existing_customer is None:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    try:
        connection.execute(
            """
            UPDATE customers
            SET name = ?, email = ?, phone = ?
            WHERE id = ?
            """,
            (
                customer.name,
                customer.email,
                customer.phone,
                customer_id
            )
        )

        connection.commit()

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="E-mail já cadastrado"
        )

    finally:
        connection.close()

    return {
        "id": customer_id,
        "name": customer.name,
        "email": customer.email,
        "phone": customer.phone
    }


@router.delete(
    "/{customer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Excluir cliente",
    description="Exclui um cliente pelo seu ID."
)
def delete_customer(customer_id: int):
    connection = get_connection()

    customer = connection.execute(
        "SELECT * FROM customers WHERE id = ?",
        (customer_id,)
    ).fetchone()

    if customer is None:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    connection.execute(
        "DELETE FROM customers WHERE id = ?",
        (customer_id,)
    )

    connection.commit()
    connection.close()

    return None

