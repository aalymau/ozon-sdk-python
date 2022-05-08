
from .response import ProductInfoResponse, ProductListResponse, ProductInfoStocksResponse
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
