from pydantic import BaseModel, EmailStr, Field


class CustomerCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    phone: str = Field(
        min_length=8,
        max_length=20
    )


class CustomerUpdate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    phone: str = Field(
        min_length=8,
        max_length=20
    )


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str