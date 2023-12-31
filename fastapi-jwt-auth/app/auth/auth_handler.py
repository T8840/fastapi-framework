# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")




def token_response(token: str):
    return {
        "access_token": token
    }


def customer_register_token_response(email: str):
    return {
        "id": 1,
        "email": email,
        "password": "$2b$10$vlUeEOUik52khucq479cPejGDHD95xDKivoL4SaNjdV6/QsDQXXLe",
        "role": "Customer",
        "updatedAt": "2023-10-23T10:13:50.798Z",
        "createdAt": "2023-10-23T10:13:50.798Z",
    }

def customer_token_response(token: str):
    return {
        "email": "test@test.com",
        "role": "Customer",
        "access_token": token
    }




# function used for signing the JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def signCustomerJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return customer_token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
