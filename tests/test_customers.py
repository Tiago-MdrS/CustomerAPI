from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Customer API funcionando!"
    }


def test_create_customer():
    response = client.post(
        "/customers/",
        json={
            "name": "Cliente Teste",
            "email": "cliente.teste@example.com",
            "phone": "99999-9999"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Cliente Teste"
    assert data["email"] == "cliente.teste@example.com"
    assert data["phone"] == "99999-9999"
    assert "id" in data


def test_list_customers():
    response = client.get("/customers/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_customer():
    create_response = client.post(
        "/customers/",
        json={
            "name": "Busca Teste",
            "email": "busca.teste@example.com",
            "phone": "98888-8888"
        }
    )

    assert create_response.status_code == 201

    customer_id = create_response.json()["id"]

    response = client.get(
        f"/customers/{customer_id}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == customer_id


def test_get_customer_not_found():
    response = client.get("/customers/999999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Cliente não encontrado"
    }


def test_create_customer_invalid_email():
    response = client.post(
        "/customers/",
        json={
            "name": "Cliente Inválido",
            "email": "email-invalido",
            "phone": "99999-9999"
        }
    )

    assert response.status_code == 422



def test_create_customer_duplicate_email():
    customer = {
        "name": "Cliente Original",
        "email": "duplicado@example.com",
        "phone": "99999-1111"
    }

    first_response = client.post(
        "/customers/",
        json=customer
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/customers/",
        json={
            "name": "Outro Cliente",
            "email": "duplicado@example.com",
            "phone": "99999-2222"
        }
    )

    assert second_response.status_code == 409
    assert second_response.json() == {
        "detail": "E-mail já cadastrado"
    }
    
    
    
def test_update_customer():
    create_response = client.post(
        "/customers",
        json={
            "name": "Cliente Original",
            "email": "original@example.com",
            "phone": "99999-1111"
        }
    )
    assert create_response.status_code == 201
    customer_id = create_response.json()["id"]

    update_response = client.put(
    f"/customers/{customer_id}",
    json={
        "name": "Cliente Atualizado",
        "email": "atualizado@example.com",
        "phone": "98888-2222"
    }
)

    assert update_response.status_code == 200
    data = update_response.json()
    
    assert data["id"] == customer_id
    assert data["name"] == "Cliente Atualizado"
    assert data ["email"] == "atualizado@example.com"
    assert data ["phone"] == "98888-2222"



def test_update_customer_not_found():
    response = client.put(
        "/customers/999999",
        json={
            "name": "Cliente",
            "email": "cliente404@example.com",
            "phone": "99999-9999"
        }
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Cliente não encontrado"
    }
    
    
def test_delete_customer():
    create_response = client.post(
        "/customers/",
        json={
            "name": "Cliente Para Excluir",
            "email": "excluir@example.com",
            "phone": "97777-7777"
        }
    )

    assert create_response.status_code == 201

    customer_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/customers/{customer_id}"
    )

    assert delete_response.status_code == 204


    get_response = client.get(
        f"/customers/{customer_id}"
    )

    assert get_response.status_code == 404
    
def test_search_customers():
    client.post(
        "/customers/",
        json={
            "name": "Tiago Silva",
            "email": "tiago.silva@example.com",
            "phone": "99999-1111"
        }
    )
    
    client.post(
        "/customers/",
        json={
            "name": "Maria Souza",
            "email": "maria.souza@example.com",
            "phone": "98888-2222"
        }
    )
    
    response = client.get(
        "/customers/?search=Tiago"
    )
    
    assert response.status_code == 200
    
    customers = response.json()
    
    assert len(customers) == 1
    assert customers[0]["name"] == "Tiago Silva"
    
def test_search_customers_by_email():
    client.post(
        "/customers/",
        json={
            "name": "João Pereira",
            "email": "joao.pereira@example.com",
            "phone": "97777-3333"
        }
    )

    response = client.get(
        "/customers/?search=joao.pereira"
    )

    assert response.status_code == 200

    customers = response.json()

    assert len(customers) == 1
    assert customers[0]["email"] == "joao.pereira@example.com"
    
def test_create_customer_empty_name():
    response = client.post(
        "/customers/",
        json={
            "name": "",
            "email": "nome.invalido@example.com",
            "phone": "99999-9999"
        }
    )

    assert response.status_code == 422

def test_create_customer_invalid_phone():
    response = client.post(
        "/customers/",
        json={
            "name": "Cliente Teste",
            "email": "telefone.invalido@example.com",
            "phone": "123"
        }
    )

    assert response.status_code == 422

def test_create_customer_short_name():
    response = client.post(
        "/customers/",
        json={
            "name": "A",
            "email": "nome.curto@example.com",
            "phone": "99999-9999"
        }
    )

    assert response.status_code == 422