from .base import BaseEntity

class Stock(BaseEntity):
    between_warehouses: int = 0
    for_sale: int = 0
    loss: int = 0
    not_for_sale: int = 0
    shipped: int = 0

class TotalItem(BaseEntity):
    """Данные по остаткам на всех складах"""

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
