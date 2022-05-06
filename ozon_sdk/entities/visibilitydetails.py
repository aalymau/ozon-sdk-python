from .base import BaseEntity

class VisibilityDetails(BaseEntity):
    active_product: bool
    has_price: bool
    has_stock: bool