from .base import BaseResponse
from ..entities import ProductInfoStocks

class ProductInfoStocksResponse(BaseResponse):
    result: list[ProductInfoStocks]