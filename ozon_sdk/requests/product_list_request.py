from .base import BaseRequest
from .product_list_filter_request import ProductListFilterRequest

class ProductListRequest(BaseRequest):
    filter: ProductListFilterRequest
    last_id: str = ''
    limit: int = 1000