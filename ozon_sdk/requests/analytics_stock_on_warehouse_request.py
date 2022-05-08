from .base import BaseRequest

class AnalyticsStockOnWarehouseRequest(BaseRequest):
    """Отчёт по остаткам и товарам"""

    limit: int = 100
    offest: int = 0
