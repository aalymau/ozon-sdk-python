from .base import BaseResponse
from ..entities import ProductInfo

class ProductInfoResponse(BaseResponse):
    result: ProductInfo