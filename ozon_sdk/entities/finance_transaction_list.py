from .base import BaseEntity
from .finance_transaction_list_v3_response_operation import FinanceTransactionListV3ResponseOperation

class FinanceTransactionList(BaseEntity):
    """Список транзакций (версия 3)"""

    operations: list[FinanceTransactionListV3ResponseOperation] = []
    page_count: int = 0
    row_count: int = 0