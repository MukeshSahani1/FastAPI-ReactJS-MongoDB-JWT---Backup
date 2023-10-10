import os
import bcrypt
from models.user import UserLoginSchema

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_password


import jwt
from datetime import datetime, timedelta

def create_access_token(data: dict):
    expires_delta = timedelta(minutes=120)
    expire = datetime.utcnow() + expires_delta
    data.update({"exp": expire})
    token = jwt.encode(data, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return token

def check_user(data : UserLoginSchema):
    pass
