from .base import BaseResponse
from ..entities import ProductInfoList

class ProductInfoListResponse(BaseResponse):
    result: ProductInfoList