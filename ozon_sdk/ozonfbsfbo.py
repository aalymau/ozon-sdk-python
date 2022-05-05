import requests
import asyncio
from .authorization import Ozon

class OzonFboFbs(Ozon):
    """_summary_
    """

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

