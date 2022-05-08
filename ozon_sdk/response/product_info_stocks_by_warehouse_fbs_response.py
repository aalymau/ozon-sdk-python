from .base import BaseResponse
from ..entities import ProductInfoStocksByWarehouseFBS

class ProductInfoStocksByWarehouseFBSResponse(BaseResponse):
    result: list[ProductInfoStocksByWarehouseFBS]