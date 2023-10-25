from pydantic import BaseModel, Field, EmailStr
from typing import List, Set

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens...."
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Joe Doe",
                "email": "joe@xyz.com",
                "password": "any"
            }
        }

class CustomerSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    role: str = Field(...)

    class Config:
        schema_extra = {
            "example": {              
               
            }
        }        

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                "password": "any"
            }
        }

class CarsSchema(BaseModel):
    id: int = Field(default=None)
    name: str = Field(...)
    category: str = Field(...)
    price: int = Field(...)
    status: bool = Field(default=False)
    start_rent_at: str = Field(default=None)
    finish_rent_at: str = Field(default=None)
    image: str = Field(...)
    createdAt: str = Field(...)
    updatedAt: str = Field(...)


class CarsListSchema(BaseModel):
    page: int = Field(default=None)
    pageSize: str = Field(...)
    pageCount: str = Field(...)
    cars: List[CarsSchema]

    class Config:
        schema_extra = {
            "example": {
            "page": 1,
            "pageSize": 10,
            "pageCount": 2,
            "count": 11,
            "cars": [
                {
                    "id": 2901,
                    "name": "Pajero SUV",
                    "category": "medium",
                    "price": 550000,
                    "status": false,
                    "start_rent_at": null,
                    "finish_rent_at": null,
                    "image": "https://firebasestorage.googleapis.com/v0/b/km-sib-2---secondhand.appspot.com/o/cars%2F1697795087258-1665112943_mitsubishi-new-pajero-sport-rajanya-segmen-suv-medium.webp?alt=media",
                    "createdAt": "2023-08-21T15:40:28.426Z",
                    "updatedAt": "2023-10-20T09:44:47.259Z"
                },
                {
                    "id": 2800,
                    "name": "Corvette C6R Cop edition",
                    "category": "small",
                    "price": 2500000,
                    "status": false,
                    "start_rent_at": null,
                    "finish_rent_at": null,
                    "image": "https://firebasestorage.googleapis.com/v0/b/km-sib-2---secondhand.appspot.com/o/cars%2F1691510489595-4765469221049107489_23.jpg?alt=media",
                    "createdAt": "2023-08-08T16:01:29.600Z",
                    "updatedAt": "2023-08-08T16:01:29.600Z"
                },
                {
                    "id": 3016,
                    "name": "Hilux tes",
                    "category": "medium",
                    "price": 123000,
                    "status": false,
                    "start_rent_at": null,
                    "finish_rent_at": null,
                    "image": "https://firebasestorage.googleapis.com/v0/b/km-sib-2---secondhand.appspot.com/o/cars%2F1697784388737-pngwing.com_(1).png?alt=media",
                    "createdAt": "2023-10-20T06:46:28.740Z",
                    "updatedAt": "2023-10-20T06:46:28.740Z"
                }
            ]
        }

        }

