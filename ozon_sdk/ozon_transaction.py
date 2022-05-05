import requests
import asyncio
from .authorization import Ozon

class OzonTransaction(Ozon):
    """_summary_

    Args:
        Ozon (_type_): _description_
    """

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