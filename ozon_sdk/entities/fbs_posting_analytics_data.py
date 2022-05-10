from .base import BaseEntity

class FPSPostingAnalyticsData(BaseEntity):
    city: str
    delivery_date_begin: str
    delivery_date_end: str
    delivery_type: str
    is_legal: bool
    is_premium: bool
    payment_type_group_name: str
    region: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int
    