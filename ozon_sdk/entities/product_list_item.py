from .base import BaseEntity

class ProductListItems(BaseEntity):
    """Класс для списка товаров"""

    offer_id: str
    product_id: int