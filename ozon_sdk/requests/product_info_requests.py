from .ozon_base_request import BaseRequest

class ProductInfoRequest(BaseRequest):
    offer_id: str = ''
    product_id: int = 0
    sku: int = 0