from .base import BaseResponse
from ..entities import ProductList

class ProductListResponse(BaseResponse):
    result: ProductList