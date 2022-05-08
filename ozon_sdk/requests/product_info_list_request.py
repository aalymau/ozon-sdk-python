from .base import BaseRequest

class ProductInfoListRequest(BaseRequest):
    """Получить список товаров по идентификаторам"""
    
    offer_id: list[str] = []
    product_id: list[int] = []
    sku: list[int] = []