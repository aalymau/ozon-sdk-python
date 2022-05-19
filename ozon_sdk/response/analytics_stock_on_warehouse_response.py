from .base import BaseResponse
from ..entities import TotalItem, WhItem
from datetime import datetime

class AnalyticsStockOnWarehouseResponse(BaseResponse):
    """Отчёт по остаткам и товарам"""

    timestamp: datetime
    total_items: list[TotalItem]
    wh_items: list[WhItem]

    class Config:
        orm_mode = True