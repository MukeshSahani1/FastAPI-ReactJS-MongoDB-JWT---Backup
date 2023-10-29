from fastapi import Body, FastAPI , HTTPException , Depends , status
from .config.db import fetch_one_user , create_new_user , fetch_all_users , save_blacklisted_token
from .config.db import fetch_one_shipment, fetch_all_shipment, create_new_shipment
from passlib.context import CryptContext
from .models.user import UserSchema , UserLoginSchema, UserRequestSchema
from .models.shipment import ShipmentSchema
from fastapi.middleware.cors import CORSMiddleware
from .auth.fa import send_otp

from .auth.auth_handler import signJWT
from .auth.auth_bearer import JWTBearer
from .auth.fa import send_otp
from random import random, randrange

app = FastAPI() 

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create a CryptContext object
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# App Home page
@app.get("/", tags=["Home"])
async def index():
    return {"message": "Hello User"}


# Shipment Data fill
@app.post("/shipment/register", tags=["shipment-register"], status_code=status.HTTP_201_CREATED)
async def register(shipment: ShipmentSchema = Body(...)):
    # Check if shipment Number is registered
    existing_shippingNO = await fetch_one_shipment(shipment.shipment_no)
    if existing_shippingNO:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Shipment No. already Present")

    # Create a new shipment data
    shipment_data = {
        "shipment_no": shipment.shipment_no,
        "container_no": shipment.container_no,
        "route_details": shipment.route_details,
        "goods_type": shipment.goods_type,
        "device": shipment.device,
        "expected_delivery_date": shipment.expected_delivery_date,
        "po_number": shipment.po_number,
        "delivery_number": shipment.delivery_number,
        "ndc_number": shipment.ndc_number,
        "batch_id": shipment.batch_id,
        "serial_number_goods": shipment.serial_number_goods,
        "shipment_description": shipment.shipment_description
    }

    result = await create_new_shipment(shipment_data)

    if result:
        # Generate JWT token
        USER_JWT_TOKEN = signJWT(shipment.shipment_no)
        return {"message": "Shipment created successfully", "token": USER_JWT_TOKEN,}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")



# User signup API endpoint
@app.post("/user/sign-up", tags=["user-sign-up"], status_code=status.HTTP_201_CREATED)
async def signup(user: UserSchema = Body(...)):
    # Check if the user email already exists
    existing_user = await fetch_one_user(user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")

    hashed_password = pwd_context.hash(user.password) # Hash the password using the CryptContext

    # Create a new user document
    user_data = {
        "Full_name": user.fullname,
        "email": user.email,
        "password": hashed_password
    }

    result = await create_new_user(user_data) # Insert the user document into the collection

    if result:
        # Generate JWT token
        USER_JWT_TOKEN = signJWT(user.email)
        return {"message": "User created successfully", "token": USER_JWT_TOKEN,}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


# User sign-in API endpoint
@app.post("/user/sign-in", tags=["user-sign-in"])
async def login(user: UserLoginSchema = Body(...)):
    # Retrieve the user from the database using the email
    existing_user = await fetch_one_user(user.email)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Compare the provided password with the stored hashed password
    if not pwd_context.verify(user.password, existing_user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong login details")

    # Generate JWT token
    USER_JWT_TOKEN = signJWT(user.email)
    
    # Return signJWT(user.email)
    return {"message": "User logged in successfully", "token": USER_JWT_TOKEN, "status_code": 200}



# User Request Password API endpoint
@app.post("/user/requestpassword", tags=["user-request-password"])
async def request(user: UserRequestSchema = Body(...)):
# Retrieve the user from the database using the email
    existing_user = await fetch_one_user(user.email)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    send_otp(user.email, 1234)
    # Generate JWT token 
    USER_JWT_TOKEN = signJWT(user.email)
    
    return {"message": f"An OTP has been sent to {user.email}.", "token": USER_JWT_TOKEN, "status_code": 200}




# Protected Route
@app.post("/test/authentication", dependencies=[Depends(JWTBearer())], tags=["Protected-Testing-Route"])
def add_post(post: UserLoginSchema):
    email = post.email 
    password = post.password
    return {
        "email": email,
        "password" : password
    }


# Blacklist the token 
@app.post("/token/blacklist", tags=["Blacklist the token "])
async def set_blacklist_token(token:dict):
    result = await save_blacklisted_token(token)
    if result:
        return {"message":"Token blacklisted Succesfully" , "status_code":200}
    else:
        return {"message":"There is an error" , "status_code":400}



# Fetch all users 
@app.get("/test/users/all", dependencies=[Depends(JWTBearer())] ,  tags=["All-users-Testing"])
async def all_users():
    result = await fetch_all_users()
    return result
