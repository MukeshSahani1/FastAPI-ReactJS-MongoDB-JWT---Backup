#The goal of this file is to check whether the reques tis authorized or not [ verification of the proteced route]
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decodeJWT
from typing import Optional
# from config.db import is_token_blacklisted

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: Optional[HTTPAuthorizationCredentials] = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            if self.is_token_blacklisted(credentials.credentials):
                raise HTTPException(status_code=403, detail="Token is blacklisted.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
    
    def is_token_blacklisted(self, jwtoken: str) -> bool:
        # result = is_token_blacklisted(jwtoken)
        # print(result)
        # if result:
        #     return True
        # else:
        # # Check if the token is blacklisted in the collection
        # # Implement your logic to query the blacklisted collection and check if the token exists
        # # Return True if the token is blacklisted, False otherwise
            return False  # Replace with your implementation
