from .base import BaseEntity

class FboPostingFboPostingAnalyticsData(BaseEntity):
    city: str
    delivery_type: str
    is_legal: bool
    is_premium: bool
    payment_type_group_name: str
    region: str
    warehouse_id: int
    warehouse_name: str