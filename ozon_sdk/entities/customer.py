from .base import BaseEntity

class Address(BaseEntity):
    address_tail: str
    city: str
    comment: str
    country: str
    district: str
    latitude: float
    longitude: float
    provider_pvz_code: str
    pvz_code: int
    region: str
    zip_code: str

class Customer(BaseEntity):
    address: Address
    customer_email: str
    customer_id: int
    name: str
    phone: str
    