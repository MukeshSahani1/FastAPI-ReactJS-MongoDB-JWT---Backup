import pymongo
from datetime import datetime

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["scm"]

# Define the collections for shipments and products
shipments = db["shipments"]
products = db["products"]

def create_product(name, quantity):
    product = {
        "name": name,
        "quantity": quantity,
    }
    return products.insert_one(product)

def create_shipment(product_id, quantity):
    product = products.find_one({"_id": product_id})
    if product:
        if product["quantity"] >= quantity:
            shipment = {
                "product_id": product_id,
                "quantity": quantity,
                "timestamp": datetime.now(),
            }
            shipments.insert_one(shipment)
            products.update_one({"_id": product_id}, {"$inc": {"quantity": -quantity}})
            print("Shipment created successfully.")
        else:
            print("Error: Insufficient quantity in inventory.")
    else:
        print("Error: Product not found in inventory.")

def list_inventory():
    for product in products.find():
        print(f"Product ID: {product['_id']}, Name: {product['name']}, Quantity: {product['quantity']}")

def list_shipments():
    for shipment in shipments.find():
        product = products.find_one({"_id": shipment["product_id"]})
        print(f"Shipment ID: {shipment['_id']}, Product: {product['name']}, Quantity: {shipment['quantity']}, Timestamp: {shipment['timestamp']}")

# Example usage:
if __name__ == "__main__":
    # Create some initial products
    create_product("Widget A", 100)
    create_product("Widget B", 50)

    # List the inventory
    print("Inventory:")
    list_inventory()

    # Create a shipment
    create_shipment(products.find_one({"name": "Widget A"})["_id"], 20)

    # List the shipments
    print("\nShipments:")
    list_shipments()
