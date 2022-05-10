from .base import BaseEntity

class FBSPostingProduct(BaseEntity):
    mandatory_mark: list[str]
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int