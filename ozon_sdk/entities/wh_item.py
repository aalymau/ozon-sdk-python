from .base import BaseEntity

class Stock(BaseEntity):
    for_sale: int = 0
    loss: int = 0
    not_for_sale: int = 0

class Item(BaseEntity):
    barcode: str
    category: str
    discounted: str
    height: float
    length: float
    offer_id: str
    sku: str
    stocks: Stock = {}
    title: str
    volume: float
    weight: float
    width: float

class WhItem(BaseEntity):
    """Данные остатков по определённым складам"""

    id: str
    items: list[Item]
    name: str