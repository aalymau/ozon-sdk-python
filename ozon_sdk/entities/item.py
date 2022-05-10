from datetime import datetime

from .base import BaseEntity
from .status import Status
from .source import Source
from .stocks import Stocks

class reasons(BaseEntity):
    description: str
    id: int

class Reasons(BaseEntity):
    property_name: reasons = {}

class VisibilityDetails(BaseEntity):
    active_product: bool
    has_price: bool
    has_stock: bool
    reasons: Reasons = {}

class Item(BaseEntity):
    """	
        Array of objects (productv2GetProductInfoListResponseItem)
        Массив данных.
    """

    barcode: str
    buybox_price: str
    category_id: int
    color_image: str
    created_at: datetime
    fbo_sku: int
    fbs_sku: int
    id: int
    images: list[str]
    primary_image: str
    images360: list[str]
    marketing_price: str
    min_ozon_price: str
    min_price: str
    name: str
    offer_id: str
    old_price: str
    premium_price: str
    price: str
    price_index: str
    recommended_price: str
    status: Status
    sources: list[Source]
    stocks: Stocks
    vat: str
    visibility_details: VisibilityDetails
    visible: bool
