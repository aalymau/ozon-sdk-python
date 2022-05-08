from .base import BaseEntity

class Stocks(BaseEntity):
    present: int = 0
    reserved: int = 0
    type: str = ''

class ProductInfoStocksItem(BaseEntity):
    offer_id: str
    product_id: int
    sotcks: Stocks