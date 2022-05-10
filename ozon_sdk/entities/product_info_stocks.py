from .base import BaseEntity
from .product_info_stocks_item import ProductInfoStocksItem

class ProductInfoStocks(BaseEntity):
    """Информация о количестве товара"""

    items: list[ProductInfoStocksItem]
    last_id: str
    total: int