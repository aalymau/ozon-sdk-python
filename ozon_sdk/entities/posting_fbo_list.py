from .base import BaseEntity
from .posting_fbo_list_analytics_data import FboPostingFboPostingAnalyticsData
from .posting_financial_data import FinacialData
from .posting_product import PostingProduct
from datetime import datetime

class AdditionalData(BaseEntity):
    key: str
    value: str


    

class PostingFBOList(BaseEntity):
    additional_data: list[AdditionalData] = []
    analytics_data: FboPostingFboPostingAnalyticsData = None
    cancel_reason_id: int = 0
    created_at: datetime
    financial_data: FinacialData = None
    in_process_at: str = ''
    order_id: int = 0
    order_number: str = ''
    posting_number: str = ''
    products: list[PostingProduct] = []
    status: str = ''