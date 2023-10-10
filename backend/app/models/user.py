from pydantic import BaseModel , Field , EmailStr

# User model
class UserSchema(BaseModel):
    fullname : str = Field(..., min_length=2)
    email: str = Field(..., min_length=5)
    password: str = Field(..., min_length=8)
    dob: str = Field(..., min_length=4)
    gender: str = Field(...,min_length=1)
    country : str = Field(..., min_length=2)

    class Config:
        schema_extra = {
            "example": {
                "fullname" : "Joe Doe",
                "email" : "joe@xyz.com",
                "password" : "anyanyany",
                "dob" : "03-03-2001",
                "gender" : "male",
                "country" : "India"
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