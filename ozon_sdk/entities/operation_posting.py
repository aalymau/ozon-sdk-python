from .base import BaseEntity

class OperationPosting(BaseEntity):
    delivery_schema: str
    order_date: str
    posting_number: str
    warehouse_id: int