from .base import BaseEntity
from . import Item

class ProductInfoList(BaseEntity):
    """Получить список товаров по идентификаторам"""

    items: list[Item]