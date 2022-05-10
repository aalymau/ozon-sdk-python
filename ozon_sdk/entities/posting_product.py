from .base import BaseEntity

class PostingProduct(BaseEntity):
    digital_code: str = ''
    name: str = ''
    offer_id: str = ''
    price: str = ''
    quantity: int = 0
    sku: int = 0