from datetime import datetime
from .base import BaseEntity
from .comission import Comission
from .status import Status
from .source import Source
from .stocks import Stocks
from .visibilitydetails import VisibilityDetails

class ProductInfo(BaseEntity):
    """Информация о товаре

    Args:
        BaseEntity (_type_): _description_
    """
    barcode: str = ''
    buybox_price: str = ''
    category_id: int = 0
    color_image: str = ''
    comissions: list[Comission] = []
    created_at: datetime
    fbo_sku: int = 0
    fbs_sku: int = 0
    id: int = 0
    images: list[str] = []
    primary_image: str = ''
    image360: list[str] = []
    is_prepayment: bool
    is_prepayment_allowed: bool
    marketing_price: str = ''
    min_ozon_price: str = ''
    min_price: str = ''
    name: str = ''
    offer_id: str = ''
    old_price: str = ''
    premium_price: str = ''
    price: str = ''
    price_index: str = ''
    recommended_price: str = ''
    status: Status = None
    sources: list[Source] = []
    stocks: Stocks
    vat: str = ''
    visibility_details: VisibilityDetails = None
    visible: bool
    volume_weight: float = 0


