from .base import BaseResponse
from ..entities import TotalItem, WhItem

class AnalyticsStockOnWarehouseResponse(BaseResponse):
    """Отчёт по остаткам и товарам"""

    timestamp: str
    total_items: list[TotalItem]
    wh_items: list[WhItem]