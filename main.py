import asyncio
from ozon_sdk import get_product_info
from ozon_sdk.authorization import Ozon
from ozon_sdk.ozon_api  import OzonApi
# print(api_user.test())
# print(Ozon.get())
async def main():
    api_user = OzonApi('user_id', 'api_key')
    # answer = api_user.get_product_info(offer_id='', product_id=247465013, sku=0)
    # print(answer)
    answer = asyncio.create_task(api_user.get_product_list())
    await answer
    print(answer)
    answer = asyncio.create_task(api_user.get_product_info(offer_id='', product_id=247465013, sku=0))
    await answer
    print(answer)
asyncio.run(main())
# api_user = get_product_info.OzonMethods('48237', 'f624596d-2f1e-4644-8d19-8bb45fb39004')
# answer = api_user.get_product_info(offer_id='', product_id=247465013, sku=0)
# print(answer)