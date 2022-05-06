import asyncio
from ozon_sdk.ozon_api  import OzonApi

async def main():
    api_user = OzonApi('user_id', 'api_key')
    answer = asyncio.create_task(api_user.get_product_list())
    await answer
    print(answer.result())
    # answer = asyncio.create_task(api_user.get_product_info(offer_id='', product_id=247465013, sku=0))
    # await answer
    # print(answer)

asyncio.run(main())
