import requests
import json

class Ozon(object):

    error_response_statuses = {
        400: 'Invalid parameter',
        403: 'Access denied',
        404: 'No answer found',
        409: 'Request Conflict',
        500: 'Internal server error'
    }

    def __init__(self, client_id: str='', api_key: str=''):

        self.__headers = {
            'Client-Id': client_id,
            'Api-Key': api_key
        }

    

    def default_method(self, url: str, data: dict ):
        """_summary_

        Args:
            url (str): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        try:
            response = requests.post(url, headers=self.__headers, json=data)
        except:
            return {
                'status': 0,
                'message': 'Connection Error: Проверьте работу сети'
            }
        
        if response.status_code in self.error_response_statuses:
            return {
                'status': response.status_code,
                'message': response.json()['message']
            }
        
        return response.json()['result']
