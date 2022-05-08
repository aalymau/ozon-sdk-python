from .base import BaseEntity

class ProductInfoStocksByWarehouseFBS(BaseEntity):
    """Информация об остатках на складах продавца (FBS и rFBS)"""

    fbs_sku: int
    present: int
    product_id: int
    reserved: int
    warehouse_id: int
    warehouse_name: str