from pydantic import BaseModel , Field , EmailStr

# Shipment Mode

# User model
class ShipmentSchema(BaseModel):
    shipment_no : str = Field(...,)
    container_no : str = Field(...,)
    route_details : str = Field(...,)
    goods_type : str = Field(...,)
    device : str = Field(...,)
    expected_delivery_date : str = Field(...,)
    po_number : str = Field(...,)
    delivery_number : str = Field(...,)
    ndc_number : str = Field(...,)
    batch_id : str = Field(...,)
    serial_number_goods : str = Field(...,)
    shipment_description : str = Field(...,)

    class Config:
        schema_extra = {
            "example": {
                "shipment_no": "1234567890",
                "container_no": "123456",
                "route_details": "Mumbai",
                "goods_type": "Electronics",
                "device": "14567890",
                "expected_delivery_date": "03-03-2023",
                "po_number": "PO123456",
                "delivery_number": "09890",
                "ndc_number": "123456",
                "batch_id": "100",
                "serial_number_goods": "456321",
                "shipment_description": "Electronic goods Deliver to Mumbai"
            
            }
        }