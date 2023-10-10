# This file is responsible for signing , encoding , decoding and returning JWTS

import time
import os
from typing import Dict

import jwt
from decouple import config

JWT_SECRET = config("SECRET_KEY")
JWT_ALGORITHM = config("ALGORITHM")


def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def signJWT(user_email: str) -> Dict[str, str]:
    payload = {
        "user_email": user_email,
        "expires": time.time() + 7200
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=str(JWT_ALGORITHM))

    return token_response(token)

def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
