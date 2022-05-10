
from ozon_sdk.response.analytics_stock_on_warehouse_response import AnalyticsStockOnWarehouseResponse
from .response import ProductInfoResponse, ProductListResponse, ProductInfoStocksResponse, ProductInfoStocksByWarehouseFBSResponse, AnalyticsStockOnWarehouseResponse, ProductInfoListResponse, CategoryTreeResponse, FinanceTransactionListResponse
from .response import BaseResponse
from typing import Type
from .ozon_async_api import OzonAsyncApi
from .core import OzonAsyncEngine

class OzonAPIFactory:
    """Фабрика для endpoint'ов апи. Получение инстанса апи для каждого типа возвращаемого значения
    """

    api_list: dict[Type[BaseResponse], str] = {
        ProductInfoResponse: '/v2/product/info',
        ProductListResponse: '/v2/product/list',
        ProductInfoStocksResponse: '/v3/product/info/stocks',
        ProductInfoStocksByWarehouseFBSResponse: '/v1/product/info/stocks-by-warehouse/fbs',
        AnalyticsStockOnWarehouseResponse: '/v1/analytics/stock_on_warehouses',
        ProductInfoListResponse: '/v2/product/info/list',
        CategoryTreeResponse: '/v2/category/tree',
        FinanceTransactionListResponse: '/v3/finance/transaction/list',
    }

    def __init__(self, engine: OzonAsyncEngine):
        """_summary_

        Args:
            engine (OzonAsyncEngine): _description_
        """
        self._engine = engine


    def get_api(self, response_type: Type[BaseResponse]):
        """_summary_

        Args:
            response_type (Type[BaseResponse]): _description_
        """
        url = OzonAPIFactory.api_list.get(response_type)
        api = OzonAsyncApi(self._engine, url, response_type)

        return api
