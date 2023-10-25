#Twitter: Bek Brace
#Instagram: Bek_Brace

import uvicorn
from fastapi import FastAPI, Body, Depends

from app.model import PostSchema, UserSchema, UserLoginSchema, CustomerSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT, signCustomerJWT, customer_register_token_response

from fastapi.middleware.cors import CORSMiddleware
import math
posts = [
    {
        "id": 1,
        "title": "Penguins ",
        "text": "Penguins are a group of aquatic flightless birds."
    },
    {
        "id": 2,
        "title": "Tigers ",
        "text": "Tigers are the largest living cat species and a memeber of the genus panthera."
    },
    {
        "id": 3,
        "title": "Koalas ",
        "text": "Koala is arboreal herbivorous maruspial native to Australia."
    },
]

users = []

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# route handlers

# testing
@app.get("/", tags=["test"])
def greet():
    return {"hello": "world!."}


# Get Posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return { "data": posts }


@app.get("/posts/{id}", tags=["posts"])
def get_single_post(id: int):
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }


@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

@app.post("/customer/auth/register", tags=["user"])
def customer_register(user: CustomerSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return customer_register_token_response(user.email)


@app.post("/customer/auth/login", tags=["user"])
def customer_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signCustomerJWT(user.email)
    return {
        "error": "Wrong login details!"
    }


cars = [
                {
                    "id": 2901,
                    "name": "Pajero SUV",
                    "category": "medium",
                    "price": 550000,
                    "status": False,
                    "start_rent_at": None,
                    "finish_rent_at": None,
                    "image": "https://firebasestorage.googleapis.com/v0/b/km-sib-2---secondhand.appspot.com/o/cars%2F1697795087258-1665112943_mitsubishi-new-pajero-sport-rajanya-segmen-suv-medium.webp?alt=media",
                    "createdAt": "2023-08-21T15:40:28.426Z",
                    "updatedAt": "2023-10-20T09:44:47.259Z"
                },
                {
                    "id": 2800,
                    "name": "Corvette C6R Cop edition",
                    "category": "small",
                    "price": 2500000,
                    "status": False,
                    "start_rent_at": None,
                    "finish_rent_at": None,
                    "image": "https://firebasestorage.googleapis.com/v0/b/km-sib-2---secondhand.appspot.com/o/cars%2F1691510489595-4765469221049107489_23.jpg?alt=media",
                    "createdAt": "2023-08-08T16:01:29.600Z",
                    "updatedAt": "2023-08-08T16:01:29.600Z"
                },
                {
                    "id": 3016,
                    "name": "Hilux tes",
                    "category": "medium",
                    "price": 123000,
                    "status": False,
                    "start_rent_at": None,
                    "finish_rent_at": None,
                    "image": "https://firebasestorage.googleapis.com/v0/b/km-sib-2---secondhand.appspot.com/o/cars%2F1697784388737-pngwing.com_(1).png?alt=media",
                    "createdAt": "2023-10-20T06:46:28.740Z",
                    "updatedAt": "2023-10-20T06:46:28.740Z"
                }
            ]

@app.get("/customer/v2/car", tags=["cars"])
def get_cars(name: str = "", category: str = "", isRented: str = "", minPrice: str = "", maxPrice: str = ""):
    # 根据查询参数进行筛选和过滤
    filtered_cars = []
    for car in cars:
        if name in car["name"] and category in car["category"] and str(car["status"]).lower() == isRented.lower():
            if minPrice and maxPrice:
                if minPrice <= car["price"] <= maxPrice:
                    filtered_cars.append(car)
            elif minPrice and not maxPrice:
                if minPrice <= car["price"]:
                    filtered_cars.append(car)
            elif maxPrice and not minPrice:
                if car["price"] <= maxPrice:
                    filtered_cars.append(car)
            else:
                filtered_cars.append(car)

    # 分页处理
    page = 1
    pageSize = 10
    count = len(filtered_cars)
    pageCount = math.ceil(count / pageSize)
    start_index = (page - 1) * pageSize
    end_index = start_index + pageSize
    paginated_cars = filtered_cars[start_index:end_index]

    return {
        "page": page,
        "pageSize": pageSize,
        "pageCount": pageCount,
        "count": count,
        "cars": paginated_cars
    }