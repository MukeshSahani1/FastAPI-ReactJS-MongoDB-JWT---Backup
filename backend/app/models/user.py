from pydantic import BaseModel , Field , EmailStr

# User model
class UserSchema(BaseModel):
    name : str = Field(..., min_length=5)
    email: str = Field(..., min_length=5)
    password: str = Field(..., min_length=8)
    confirmpassword: str = Field(...,max_length=8)

    class Config:
        schema_extra = {
            "example": {
                "name" : "Joe Doe",
                "email" : "joe@xyz.com",
                "password" : "anyanyany",
                "confirmpassword":'anyanyany',
               
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