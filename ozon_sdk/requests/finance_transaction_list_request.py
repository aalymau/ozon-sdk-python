from .base import BaseRequest
from .finance_transaction_list_filter_request import FinanceTransactionListV3RequestFilter

class FinanceTransactionListRequest(BaseRequest):
    """Список транзакций (версия 3)"""

    filter: FinanceTransactionListV3RequestFilter
    page: int
    page_size: int