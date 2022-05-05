import requests

class Ozon(object):

    error_response_statuses = {
        400: 'Invalid parameter',
        403: 'Access denied',
        404: 'No answer found',
        409: 'Request Conflict',
        500: 'Internal server error'
    }

    def __init__(self, client_id: str='', api_key: str=''):


        # if client_id == '' or api_key == '':
        #     return {
        #         'status': 401,
        #         'messsage': 'Empty client_id or api_key'
        #     }

        self.__headers = {
            'Client-Id': client_id,
            'Api-Key': api_key
        }
        print(self.__headers)

        # return {
        #     'status': 200,
        #     'message': 'Succcess'
        # }
    

    def default_method(self, url: str, data: dict ):
        """_summary_

        Args:
            url (str): _description_
            data (dict): _description_

        Returns:
            _type_: _description_
        """
        
        response = requests.post(url, headers=self.__headers, json=data)
        print(self.__headers)
        print(response.json())
        if response.status_code in self.error_response_statuses:
            return {
                'status': response.status_code,
                'message': response.json()['message']
            }
        
        return response.json()['result']
