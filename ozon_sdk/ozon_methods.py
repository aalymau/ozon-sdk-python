import requests
import asyncio
from .authorization import Ozon

class OzonMethods(Ozon):
    """_summary_

    Args:
        Ozon (_type_): _description_
    """

    async def get_product_info(self, offer_id: str='', product_id: int=0, sku: int=0):
        """_summary_

        Args:
            offer_id (str): Идентификатор товара в системе продавца — артикул.
            product_id (int): Идентификатор товара.
            sku (int): Идентификатор товара в системе Ozon — SKU.
        """

        data = {
            'offer_id': offer_id,
            'product_id': product_id,
            'sku': sku
        }
        url = 'https://api-seller.ozon.ru/v2/product/info'
        
        
        return self.default_method(url, data)

    
    async def get_product_list(self, offer_id: list=[], product_id: list=[], visibility: str='ALL', last_id:str='', limit: int=100 ):
        """_summary_

        Args:
            offer_id (list, optional): Фильтр по параметру offer_id. Можно передавать список значений.. Defaults to [].
            product_id (list, optional): Фильтр по параметру product_id. Можно передавать список значений.. Defaults to [].
            visibility (str, optional): Default: "ALL"
Enum: "ALL" "VISIBLE" "INVISIBLE" "EMPTY_STOCK" "NOT_MODERATED" "MODERATED" "DISABLED" "STATE_FAILED" "READY_TO_SUPPLY" "VALIDATION_STATE_PENDING" "VALIDATION_STATE_FAIL" "VALIDATION_STATE_SUCCESS" "TO_SUPPLY" "IN_SALE" "REMOVED_FROM_SALE" "BANNED" "OVERPRICED" "CRITICALLY_OVERPRICED" "EMPTY_BARCODE" "BARCODE_EXISTS" "QUARANTINE" "ARCHIVED" "OVERPRICED_WITH_STOCK" "PARTIAL_APPROVED" "IMAGE_ABSENT" "MODERATION_BLOCK". Defaults to 'ALL'.
            last_id (str, optional): Идентификатор последнего значения на странице. Оставьте это поле пустым при выполнении первого запроса.
Чтобы получить следующие значения, укажите last_id из ответа предыдущего запроса. Defaults to ''.
            limit (int, optional): Количество значений на странице. Минимум — 1, максимум — 1000.. Defaults to 100.

        Returns:
            _type_: _description_
        """
        url = 'https://api-seller.ozon.ru/v2/product/list'
        data = {
            'filter': {
                'offer_id': offer_id,
                'product_id': product_id,
                'visibility': visibility
            },
            'last_id': last_id,
            'limit': limit,
        }
        
        
        return self.default_method(url, data)

    async def get_product_info_stocks(self,offer_id: list=[], product_id: list=[], visibility: str='ALL', last_id:str='', limit: int=100):
        """_summary_

        Args:
            offer_id (list, optional): Фильтр по параметру offer_id. Можно передавать список значений.. Defaults to [].
            product_id (list, optional): Фильтр по параметру product_id. Можно передавать список значений.. Defaults to [].
            visibility (str, optional): Default: "ALL"
Enum: "ALL" "VISIBLE" "INVISIBLE" "EMPTY_STOCK" "NOT_MODERATED" "MODERATED" "DISABLED" "STATE_FAILED" "READY_TO_SUPPLY" "VALIDATION_STATE_PENDING" "VALIDATION_STATE_FAIL" "VALIDATION_STATE_SUCCESS" "TO_SUPPLY" "IN_SALE" "REMOVED_FROM_SALE" "BANNED" "OVERPRICED" "CRITICALLY_OVERPRICED" "EMPTY_BARCODE" "BARCODE_EXISTS" "QUARANTINE" "ARCHIVED" "OVERPRICED_WITH_STOCK" "PARTIAL_APPROVED" "IMAGE_ABSENT" "MODERATION_BLOCK". Defaults to 'ALL'.
            last_id (str, optional): Идентификатор последнего значения на странице. Оставьте это поле пустым при выполнении первого запроса.
Чтобы получить следующие значения, укажите last_id из ответа предыдущего запроса.. Defaults to ''.
            limit (int, optional): Количество значений на странице. Минимум — 1, максимум — 1000.. Defaults to 100.

        Returns:
            _type_: _description_
        """

        url = 'https://api-seller.ozon.ru/v3/product/info/stocks'
        data = {
            'filter': {
                'offer_id': offer_id,
                'product_id': product_id,
                'visibility': visibility
            },
            'last_id': last_id,
            'limit': limit,
        }
        
        return self.default_method(url, data)
    
    def get_product_info_stocks_by_warehouse_fbs(self, fbs_sku: list=[]):
        """_summary_

        Args:
            fbs_sku (list): SKU товара, который продаётся со склада продавца (схемы FBS и rFBS).Максимальное количестов SKU в одном запросе — 500.
        """

        url = 'https://api-seller.ozon.ru/v1/product/info/stocks-by-warehouse/fbs'
        data = {
            'fbs_sku': fbs_sku,
        }
        #limit = 500
        return self.default_method(url, data)

    async def get_analytics_stock_on_warehouse(self, limit: int=100, offset: int=0):
        """_summary_

        Args:
            limit (int, optional): Количество ответов на странице. По умолчанию 100.. Defaults to 100.
            offset (int, optional): Количество элементов, которое будет пропущено в ответе. Например, если offset = 10, то ответ начнётся с 11-го найденного элемента.. Defaults to 0.
        """

        url = 'https://api-seller.ozon.ru/v1/analytics/stock_on_warehouses'
        data = {
            'limit': limit,
            'offset': offset,
        }

        return self.default_method(url, data)

    def get_product_info_list(self, offer_id: list=[], product_id: list=[], sku: list=[]):
        """_summary_

        Args:
            offer_id (list): _description_
            product_id (list): _description_
            sku (list): _description_
        """

        url = 'https://api-seller.ozon.ru/v2/product/info/list'
        data = {
            'offer_id': offer_id,
            'product_id': product_id,
            'sku': sku,
        }

        return self.default_method(url, data)

    async def get_category_tree(self, category_id: int=0, language: str='RU'):
        """_summary_

        Args:
            category_id (int, optional): Идентификатор категории. Defaults to 0.
            language (str, optional): Default: "DEFAULT" Enum: "DEFAULT" "RU" "EN". Defaults to 'RU'.
        """

        url = 'https://api-seller.ozon.ru/v2/category/tree'
        data = {
            'category_id': category_id,
            'language': language,
        }

        return self.default_method(url, data)

    