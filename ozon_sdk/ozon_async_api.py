from .core import OzonAsyncEngine
from typing import Type
from .response import BaseResponse

class OzonAsyncApi:
    """_summary_
    """
    def __init__(self, engine: OzonAsyncEngine, url: str, response_type: Type[BaseResponse]):
        """_summary_

        Args:
            engine (OzonAsyncEngine): _description_
            url (str): _description_
        """
        self._engine = engine
        self._url = url
        self._response_type = response_type

    async def get(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        parameters = request.dict(by_alias=True)
        response = await self._engine.get(self._url, parameters)
        data = await self._parse_response(response)
        return data

    async def post(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        parameters = request.dict(by_alias=True)
        response = await self._engine.post(self._url, parameters)
        print(response)
        data = await self._parse_response(response)
        return data

    
    async def _parse_response(self, response: dict or list):
        """
        парсинг ответа либо в list, либо в словарь. В зависимости от собственного типа возвращаемого значения
        :param response: тело ответа
        :return:
        """
        if response.get("error"):
            raise Exception(response.get("errorText"))

        data = await self._parse_response_object(response)
        return data

    async def _parse_response_object(self, response: dict):
        """
        парсинг тела ответа в объект типа self._response_object
        :param response:
        :return:
        """
        if response.get("error"):
            raise Exception(response.get("errorText"))
        return self._response_type.parse_obj(response)
