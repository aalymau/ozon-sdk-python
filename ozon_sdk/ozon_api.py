from .ozon_methods import OzonMethods
from .ozonfbsfbo import OzonFboFbs
from .ozon_transaction import OzonTransaction
from .requests import ProductInfoRequest, ProductListRequest, ProductListFilterRequest, ProductInfoStocksRequest, ProductInfoStocksFilterRequest, ProductInfoStocksByWarehouseFBSRequest
from .response import ProductInfoResponse, ProductListResponse, ProductInfoStocksResponse, ProductInfoStocksByWarehouseFBSResponse
from .core import OzonAsyncEngine
from .ozon_endpoints_list import OzonAPIFactory

class OzonApi(OzonMethods, OzonFboFbs, OzonTransaction):
    """_summary_

    Args:
        OzonMethods (_type_): _description_
        OzonFboFbs (_type_): _description_
        OzonTransaction (_type_): _description_
    """

    def __init__(self, client_id: str, api_key: str):
        """_summary_

        Args:
            client_id (_type_): _description_
            api_key (_type_): _description_
        """

        self._engine = OzonAsyncEngine(client_id=client_id, api_key=api_key)
        self._api_factory = OzonAPIFactory(self._engine)

        self._product_info_api = self._api_factory.get_api(ProductInfoResponse)
        self._product_list_api = self._api_factory.get_api(ProductListResponse)
        self._product_info_stocks = self._api_factory.get_api(ProductInfoStocksResponse)
        self._product_info_stocks_by_warehouse_fbs = self._api_factory.get_api(ProductInfoStocksByWarehouseFBSResponse)

    async def get_product_info(self, offer_id: str='', product_id: int=0, sku: int=0) -> ProductInfoResponse:
        """_summary_

        Args:
            offer_id (str): Идентификатор товара в системе продавца — артикул.
            product_id (int): Идентификатор товара.
            sku (int): Идентификатор товара в системе Ozon — SKU.
        """
        
        request = ProductInfoRequest(offer_id=offer_id, product_id=product_id, sku=sku)
        answer = await self._product_info_api.post(request)
        
        
        return answer

    
    async def get_product_list(self, offer_id: list=[], product_id: list=[], visibility: str='ALL', last_id:str='', limit: int=100 ) -> ProductListResponse:
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
        request = ProductListRequest(
            filter = ProductListFilterRequest(
                offer_id = offer_id,
                product_id = product_id,
                visibility =  visibility
            ),
            last_id = last_id,
            limit = limit
        )
        answer = await self._product_list_api.post(request)
        
        
        return answer

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
        request = ProductInfoStocksRequest(
            filter = ProductInfoStocksFilterRequest(
                offer_id = offer_id,
                product_id = product_id,
                visibility =  visibility
            ),
            last_id = last_id,
            limit = limit
        )
        answer = await self._product_list_api.post(request)
        
        
        return answer
    
    async def get_product_info_stocks_by_warehouse_fbs(self, fbs_sku: list=[str]) -> ProductInfoStocksByWarehouseFBSResponse:
        """_summary_

        Args:
            fbs_sku (list): SKU товара, который продаётся со склада продавца (схемы FBS и rFBS).Максимальное количестов SKU в одном запросе — 500.
        """

        url = 'https://api-seller.ozon.ru/v1/product/info/stocks-by-warehouse/fbs'
        data = {
            'fbs_sku': fbs_sku,
        }
        #limit = 500

        request = ProductInfoStocksByWarehouseFBSRequest(
           fbs_sku = fbs_sku
        )
        answer = await self._product_info_stocks_by_warehouse_fbs.post(request)

        return answer

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


    async def get_finance_transaction_list(self, _from: str, to: str='', operation_type: list=[], posting_number: str='', transaction_type: str='all', page: int=1, page_size: int=1000):
        """_summary_

        Args:
            _from (str): Начало периода.
                Формат: YYYY-MM-DDTHH:mm:ss.sssZ.
                Пример: 2019-11-25T10:43:06.51.
            operation_type (list): Тип операции:
            posting_number (str): Номер отправления.
            transaction_type (str): Тип начисления:
                all — все,
                orders — заказы,
                returns — возвраты и отмены,
                services — сервисные сборы,
                compensation — компенсация,
                transferDelivery — стоимость доставки,
                other — прочее.
            page (int): Номер страницы, возвращаемой в запросе.
            page_size (int):Количество элементов на странице.
            to (str, optional): Конец периода.
                Формат: YYYY-MM-DDTHH:mm:ss.sssZ.
                Пример: 2019-11-25T10:43:06.51. Defaults to ''.
        """

        url = 'https://api-seller.ozon.ru/v3/finance/transaction/list'
        data = {
            'filter': {
                'date': {
                    'from': _from,
                    'to': to,
                },
                'operation_type': operation_type,
                'posting_number': posting_number,
                'transaction_type': transaction_type,
            },
            'page': page,
            'page_size': page_size,
        }

        return self.default_method(url, data)
    
    async def get_posting_fbo_list(self, dir: str, since: str, status: str, to: str, limit:       int=1000, offset: int=0, translit: bool=True, _with: dict={} ):
        """_summary_

        Args:
            dir (str): Направление сортировки:
                asc — по возрастанию,
                desc — по убыванию.
            since (str): Начало периода в формате YYYY-MM-DD.
            status (str): Статус отправления.
                awaiting_packaging — ожидает упаковки,
                awaiting_deliver — ожидает отгрузки,
                delivering — доставляется,
                delivered — доставлено,
                cancelled — отменено.
            to (str): Конец периода в формате YYYY-MM-DD.
            limit (int, optional): Количество значений в ответе:
                максимум — 1000,
                минимум — 1.. Defaults to 1000.
            offset (int, optional): Количество элементов, которое будет пропущено в ответе. Например, если offset = 10, то ответ начнётся с 11-го найденного элемента.. Defaults to 0.
            translit (bool, optional): Если включена транслитерация адреса из кириллицы в латиницу — true.. Defaults to True.
            _with (dict, optional): Дополнительные поля, которые нужно добавить в ответ. Defaults to {}.
        """

        url = 'https://api-seller.ozon.ru/v2/posting/fbo/list'
        data = {
            'dir': dir,
            'filter': {
                'since': since,
                'status': status,
                'to': to,
            },
            'limit': limit,
            'offset': offset,
            'translit': translit,
            'with': _with,
        }

        return self.default_method(url, data)

    async def get_posting_fbs_list(self, dir: str, delivery_method_id:list, order_id:int, provider_id: list, since: str, status: str, to: str, warehouse_id:list, limit:       int=1000, offset: int=0, translit: bool=True, _with: dict={}):
        """_summary_

        Args:
            dir (str): Направление сортировки:
                asc — по возрастанию,
                desc — по убыванию.
            delivery_method_id (list): Идентификатор способа доставки.
            order_id (int): Идентификатор заказа.
            provider_id (list): Идентификатор службы доставки.
            since (str): Дата начала периода, за который нужно получить список отправлений.
                Формат UTC: ГГГГ-ММ-ДДTЧЧ:ММ:ССZ.
                Пример: 2019-08-24T14:15:22Z.
            status (str): Статус отправления:
                awaiting_registration — ожидает регистрации,
                acceptance_in_progress — идёт приёмка,
                awaiting_approve — ожидает подтверждения,
                awaiting_packaging — ожидает упаковки,
                awaiting_deliver — ожидает отгрузки,
                arbitration — арбитраж,
                client_arbitration — клиентский арбитраж доставки,
                delivering — доставляется,
                driver_pickup — у водителя,
                delivered — доставлено,
                cancelled — отменено,
                not_accepted — не принят на сортировочном центре.
            to (str): Дата конца периода, за который нужно получить список отправлений.
                Формат UTC: ГГГГ-ММ-ДДTЧЧ:ММ:ССZ.
                Пример: 2019-08-24T14:15:22Z.
            warehouse_id (list): Идентификатор склада.
            limit (int, optional): Количество значений в ответе:
                максимум — 1000,
                минимум — 1.. Defaults to 1000.
            offset (int, optional): Количество элементов, которое будет пропущено в ответе. Например, если offset = 10, то ответ начнётся с 11-го найденного элемента.. Defaults to 0.
            translit (bool, optional): _description_. Defaults to True.
            _with (dict, optional): Дополнительные поля, которые нужно добавить в ответ.. Defaults to {}.
        """

        url = 'https://api-seller.ozon.ru/v3/posting/fbs/list'
        data = {
            'dir': dir,
            'filter': {
                'delivery_method_id': delivery_method_id,
                'order_id': order_id,
                'provider_id': provider_id,
                'since': since,
                'status': status,
                'to': to,
                'warehouse_id': warehouse_id,
            },
            'limit': limit,
            'offset': offset,
            'translit': translit,
            'with': _with,
        }

        return self.default_method(url, data)

