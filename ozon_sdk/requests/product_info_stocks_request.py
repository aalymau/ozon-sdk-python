from .base import BaseRequest
from .product_info_stocks_filter_request import ProductInfoStocksFilterRequest

class ProductInfoStocksRequest(BaseRequest):
    filter: ProductInfoStocksFilterRequest
    last_id: str = ''
    limit: int = 1000