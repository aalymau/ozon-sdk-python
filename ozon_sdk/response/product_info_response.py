from .ozon_base_response import BaseResponse
from ..entities import ProductInfo

class ProductInfoResponse(BaseResponse):
    result: ProductInfo