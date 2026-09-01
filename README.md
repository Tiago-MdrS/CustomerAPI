#  Customer API

API REST desenvolvida em **Python com FastAPI** para gerenciamento de clientes.

O projeto foi desenvolvido com foco no aprendizado e aplicação prática de conceitos fundamentais de **desenvolvimento Backend**, incluindo criação de APIs REST, operações CRUD, validação de dados, tratamento de erros, persistência em banco de dados, documentação automática e testes automatizados.

---

##  Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.1.x-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge\&logo=pytest\&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)

### Principais tecnologias

* **Python**
* **FastAPI**
* **Pydantic**
* **SQLite**
* **Pytest**
* **Uvicorn**
* **Git**
* **GitHub**

---

##  Funcionalidades

A API possui as seguintes funcionalidades:

*  Criar cliente
*  Listar clientes
*  Buscar cliente por ID
*  Atualizar cliente
*  Excluir cliente
*  Pesquisar clientes por nome ou e-mail
*  Validação de e-mail
*  Validação de nome
*  Validação de telefone
*  Prevenção de e-mails duplicados
*  Tratamento de clientes não encontrados
*  Documentação automática com Swagger
*  Documentação alternativa com ReDoc
*  Testes automatizados com Pytest
*  Persistência dos dados utilizando SQLite

---

#  Estrutura do projeto

```text
CustomerAPI/
│
├── app/
│   ├── models/
│   │   └── __init__.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── customers.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── customer.py
│   │
│   ├── __init__.py
│   ├── database.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_customers.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── customers.db
```

> **Observação:** o arquivo `customers.db` é criado automaticamente pela aplicação. Caso você prefira não versionar o banco, ele pode ser incluído no `.gitignore`.

---

#  Como executar o projeto

## 1. Clonar o repositório

Clone o projeto:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd CustomerAPI
```

---

## 2. Criar o ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

---

## 3. Ativar o ambiente virtual

No **PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a execução de scripts, execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois ative novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Quando o ambiente estiver ativo, o terminal deverá apresentar algo semelhante a:

```text
(.venv) PS C:\...\CustomerAPI>
```

---

## 4. Instalar as dependências

Com o ambiente virtual ativado:

```powershell
python -m pip install -r requirements.txt
```

---

# ▶ Executando a API

Execute o servidor utilizando o Uvicorn:

```powershell
uvicorn app.main:app --reload
```

Ou:

```powershell
python -m uvicorn app.main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

---

#  Documentação da API

O FastAPI disponibiliza automaticamente uma documentação interativa através do **Swagger UI**.

### Swagger

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

A documentação permite visualizar e testar os endpoints diretamente pelo navegador.

---

#  Endpoints

##  Home

### `GET /`

Verifica se a API está funcionando.

### Resposta

```json
{
  "message": "Customer API funcionando!"
}
```

**Status:** `200 OK`

---

#  Clientes

## Criar cliente

### `POST /customers/`

Cria um novo cliente.

### Requisição

```json
{
  "name": "Cliente Teste",
  "email": "cliente@example.com",
  "phone": "99999-9999"
}
```

### Resposta

```json
{
  "id": 1,
  "name": "Cliente Teste",
  "email": "cliente@example.com",
  "phone": "99999-9999"
}
```

**Status:** `201 Created`

---

## Listar clientes

### `GET /customers/`

Retorna todos os clientes cadastrados.

### Resposta

```json
[
  {
    "id": 1,
    "name": "Cliente Teste",
    "email": "cliente@example.com",
    "phone": "99999-9999"
  }
]
```

**Status:** `200 OK`

---

## Buscar cliente por ID

### `GET /customers/{customer_id}`

Busca um cliente utilizando seu ID.

### Exemplo

```http
GET /customers/1
```

### Resposta

```json
{
  "id": 1,
  "name": "Cliente Teste",
  "email": "cliente@example.com",
  "phone": "99999-9999"
}
```

### Cliente não encontrado

```json
{
  "detail": "Cliente não encontrado"
}
```

**Status:** `404 Not Found`

---

## Atualizar cliente

### `PUT /customers/{customer_id}`

Atualiza os dados de um cliente existente.

### Exemplo

```http
PUT /customers/1
```

### Requisição

```json
{
  "name": "Cliente Atualizado",
  "email": "atualizado@example.com",
  "phone": "98888-8888"
}
```

### Resposta

```json
{
  "id": 1,
  "name": "Cliente Atualizado",
  "email": "atualizado@example.com",
  "phone": "98888-8888"
}
```

**Status:** `200 OK`

---

## Excluir cliente

### `DELETE /customers/{customer_id}`

Remove um cliente do banco de dados.

### Exemplo

```http
DELETE /customers/1
```

Em caso de sucesso, a API retorna:

**Status:** `204 No Content`

---

#  Pesquisa

Também é possível pesquisar clientes utilizando o parâmetro `search`.

## Pesquisar por nome

```http
GET /customers/?search=Tiago
```

## Pesquisar por e-mail

```http
GET /customers/?search=tiago@example.com
```

A pesquisa permite localizar clientes pelo **nome ou e-mail**.

---

#  Validações

A API utiliza **Pydantic** para validar os dados recebidos.

## Nome

O nome deve possuir pelo menos 2 caracteres.

### Exemplo inválido

```json
{
  "name": "A",
  "email": "cliente@example.com",
  "phone": "99999-9999"
}
```

**Resposta:** `422 Unprocessable Entity`

---

## E-mail

O e-mail precisa possuir um formato válido.

### Exemplo inválido

```json
{
  "name": "Cliente",
  "email": "email-invalido",
  "phone": "99999-9999"
}
```

**Resposta:** `422 Unprocessable Entity`

---

## Telefone

O telefone possui validação de tamanho.

### Exemplo inválido

```json
{
  "name": "Cliente",
  "email": "cliente@example.com",
  "phone": "123"
}
```

**Resposta:** `422 Unprocessable Entity`

---

## E-mail duplicado

Não é permitido cadastrar dois clientes utilizando o mesmo e-mail.

### Exemplo

```http
POST /customers/
```

Caso o e-mail já esteja cadastrado:

```json
{
  "detail": "E-mail já cadastrado"
}
```

**Status:** `409 Conflict`

---

#  Testes

O projeto possui testes automatizados utilizando **Pytest**.

Para executar os testes:

```powershell
python -m pytest -v
```

### Resultado atual

```text
15 passed
```

Os testes verificam funcionalidades como:

*  Página inicial
*  Criação de clientes
*  Listagem de clientes
*  Busca por ID
*  Cliente inexistente
*  E-mail inválido
*  E-mail duplicado
*  Atualização
*  Exclusão
*  Pesquisa por nome
*  Pesquisa por e-mail
*  Nome vazio
*  Telefone inválido
*  Nome muito curto

---

#  Banco de dados

O projeto utiliza **SQLite** para armazenar os clientes.

O banco é criado automaticamente pela aplicação.

### Tabela

```text
customers
```

### Estrutura

| Campo   | Tipo    | Descrição           |
| ------- | ------- | ------------------- |
| `id`    | INTEGER | Identificador único |
| `name`  | TEXT    | Nome do cliente     |
| `email` | TEXT    | E-mail do cliente   |
| `phone` | TEXT    | Telefone do cliente |

O campo `id` é gerado automaticamente pelo SQLite.

O campo `email` possui restrição de unicidade para impedir o cadastro de clientes com o mesmo endereço de e-mail.

---

#  Organização do código

O projeto utiliza uma estrutura organizada por responsabilidades.

### `app/main.py`

Responsável pela configuração principal da aplicação FastAPI e inicialização das rotas.

### `app/database.py`

Responsável pela conexão e configuração do banco de dados SQLite.

### `app/routes/`

Contém os endpoints da API.

### `app/routes/customers.py`

Contém as operações relacionadas aos clientes:

* POST
* GET
* PUT
* DELETE
* Pesquisa

### `app/schemas/`

Contém os modelos **Pydantic** utilizados para validação e estrutura dos dados.

### `app/models/`

Diretório destinado aos modelos relacionados ao banco de dados.

### `tests/`

Contém os testes automatizados da API.

---

#  Objetivo do projeto

Este projeto foi desenvolvido como parte do meu processo de aprendizado e evolução em **desenvolvimento Backend**.

O objetivo principal é consolidar conhecimentos em:

* Desenvolvimento de APIs REST
* Python
* FastAPI
* Pydantic
* SQLite
* CRUD
* Validação de dados
* Tratamento de erros
* Testes automatizados
* Documentação de APIs
* Organização de projetos Backend
* Git e GitHub

---

#  Próximos passos

Algumas melhorias planejadas para futuras versões:

*  Autenticação e autorização
*  Paginação
*  Docker
*  Migração para PostgreSQL
*  Variáveis de ambiente
*  Testes de integração
*  CI/CD com GitHub Actions
*  Deploy da API
*  Logs estruturados
*  Melhorias na documentação
*  Melhorias de segurança
*  Separação entre camadas de serviço e acesso a dados

---

#  Autor

## Tiago Madeira Silva

**Desenvolvedor Web / Backend**

Tecnologias de interesse:

* Python
* FastAPI
* C#
* .NET
* JavaScript
* React
* Node.js
* SQL
* Git
* GitHub
