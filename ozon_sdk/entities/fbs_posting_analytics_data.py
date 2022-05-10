from .base import BaseEntity
from datetime import datetime

class FPSPostingAnalyticsData(BaseEntity):
    city: str
    delivery_date_begin: datetime
    delivery_date_end: datetime
    delivery_type: str
    is_legal: bool
    is_premium: bool
    payment_type_group_name: str
    region: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int
