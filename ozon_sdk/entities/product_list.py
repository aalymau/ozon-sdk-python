from .base import BaseEntity
from .product_list_item import ProductListItems

class ProductList(BaseEntity):
    """Класс для списка продуктов"""

    items: list[ProductListItems]
    last_id: str = ''
    total: int