**Created by Aivar "ajvar_15" Nabiullin**
# ozon-sdk-python
**About**
Library for working with the Ozone API
## Install
   git clone https://gitlab.com/ajvarnabiullin/ozon-sdk-python.git
   Copy ozon_sdk dir to desired dir
##Using
Example in **main.py** file
```python
import asyncio
from ozon_sdk.ozon_api  import OzonApi

api_user = OzonApi('user_id', 'api_key')
answer = asyncio.create_task(api_user.get_product_list())
await answer
print(answer.result())

```
The functions are built according to the following type: get_{url}. Only an underscore is used instead of slashes
Example:
url = 'https://api-seller.ozon.ru/v2/product/info'
```python
get_product_info(args)
```