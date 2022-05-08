import asyncio
from ozon_sdk.ozon_api  import OzonApi

async def main(supplier):
    # product_info = asyncio.create_task(supplier.get_product_info(offer_id='', product_id=247465013, sku=0))

    # print((await product_info).result.barcode)

    # product_list = asyncio.create_task(supplier.get_product_list(
    #     offer_id:=[], product_id=[], visibility='ALL', last_id='', limit=100
    # ))

    # print((await product_list))

    product_info_stocks = asyncio.create_task(supplier.get_product_info_stocks(
        offer_id:=[], product_id=[], visibility='ALL', last_id='', limit=100
    ))

    print((await product_info_stocks))
if __name__ == '__main__':
    supplier = OzonApi(client_id='', api_key='')

    asyncio.get_event_loop().run_until_complete(main(supplier))


# async def main():
#     api_user = OzonApi('user_id', 'api_key')
#     answer = asyncio.create_task(api_user.get_product_list())
#     await answer
#     print(answer.result())
#     # answer = asyncio.create_task(api_user.get_product_info(offer_id='', product_id=247465013, sku=0))
#     # await answer
#     # print(answer)

# asyncio.run(main())

