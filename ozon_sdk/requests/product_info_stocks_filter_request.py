from .base import BaseRequest
from .product_list_filter_request import VisibilityEnum

class ProductInfoStocksFilterRequest(BaseRequest):
    offer_id: list[str] = ''
    product_id: list[str] = ''
    visibility: VisibilityEnum
