from .base import BaseEntity
from .operation_posting import OperationPosting
from .operation_service import OperationService
from datetime import datetime

class Item(BaseEntity):
    name: str
    sku: int

class FinanceTransactionListV3ResponseOperation(BaseEntity):
    accruals_for_sale: float
    amount: float
    delivery_charge: float
    items: list[Item]
    operation_date: datetime
    operation_id: int
    operation_type: str
    operation_type_name: str
    posting: OperationPosting
    return_delivery_charge: float
    sale_commission: float
    services: list[OperationService]
    type: str
