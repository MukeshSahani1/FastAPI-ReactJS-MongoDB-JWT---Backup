from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import datetime

# MongoDB configuration
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "scm"
MONGO_COLLECTION = "users"
MONGO_USERNAME = "root"
MONGO_PASSWORD = "password"

# Connect to MongoDB
mongo_client = AsyncIOMotorClient("mongodb://root:password@localhost:27017/?authMechanism=DEFAULT")
db = mongo_client[MONGO_DB]
user_details_collection = db["users"]
shipment_details_collection = db["shipment"]
blacklisted_tokens_collection = db["blacklisted_tokens"]



async def create_new_shipment(shipment_data):
    document = shipment_data
    result = await shipment_details_collection.insert_one(shipment_data)
    return document

async def fetch_all_shipment():
    cursor = shipment_details_collection.find()
    documents = []
    async for document in cursor:
        document['_id'] = str(document['_id'])
        documents.append(document)
    return documents

async def fetch_one_shipment(shipment_no):
    document = await shipment_details_collection.find_one({"shipment_no":shipment_no})
    return document

async def fetch_one_user(email):
    document = await user_details_collection.find_one({"email":email})
    return document

async def fetch_all_users():
    cursor = user_details_collection.find()
    documents = []
    async for document in cursor:
        document['_id'] = str(document['_id'])  # Convert ObjectId to string
        documents.append(document)
    return documents

async def create_new_user(user_data):
    document = user_data
    result = await user_details_collection.insert_one(user_data)
    return document

    
async def save_blacklisted_token(token) -> bool:
    ttl = datetime.timedelta(hours=2)  # Set the desired TTL duration, such as 1 hour
    
    # Set the expiry time by adding the TTL duration to the current time
    expiry_time = datetime.datetime.utcnow() + ttl

    # Add the expiry time to the token document
    token['expiry_time'] = expiry_time

    document = await blacklisted_tokens_collection.insert_one(token)

    if document:
        # Create an index on the "expiry_time" field with the TTL option
        await blacklisted_tokens_collection.create_index("expiry_time", expireAfterSeconds=0)
        return True
    else:
        return False

async def is_token_blacklisted(token):
    document = await blacklisted_tokens_collection.find_one({'token':token})
    if document:
        return True
    else:
        return False