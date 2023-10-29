from pydantic import BaseModel , Field , EmailStr

# User model
class UserSchema(BaseModel):
    fullname : str = Field(..., min_length=2)
    email: str = Field(..., min_length=5)
    password: str = Field(..., min_length=8)

    class Config:
        schema_extra = {
            "example": {
                "fullname" : "Joe Doe",
                "email" : "joe@xyz.com",
                "password" : "anyanyany"
               
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

class UserRequestSchema(BaseModel):
    email: EmailStr = Field(...)
    

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                
            }
        }