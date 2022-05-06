from .base import BaseEntity

class Comission(BaseEntity):
    deliveryAmount: float
    minValue: float
    percent: float
    returnAmount: float
    saleSchema: str
    value: float