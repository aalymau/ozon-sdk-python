import asyncio
from ozon_sdk.ozon_api  import OzonApi

async def main(supplier):
    # product_info = asyncio.create_task(supplier.get_product_info(offer_id='', product_id=247465013, sku=0))

    # print((await product_info).result.barcode)

    # product_list = asyncio.create_task(supplier.get_product_list(
    #     offer_id:=[], product_id=[], visibility='ALL', last_id='', limit=100
    # ))

    # print((await product_list))

    # product_info_stocks = asyncio.create_task(supplier.get_product_info_stocks(
    #     offer_id:=[], product_id=[], visibility='ALL', last_id='', limit=100
    # ))

    # print((await product_info_stocks))

    # product_info_stocks_by_warehouse_fbs = asyncio.create_task(supplier.get_product_info_stocks_by_warehouse_fbs(
    #     fbs_sku=['32132', '9023213']
    # ))

    # print((await product_info_stocks_by_warehouse_fbs))

    # analytics_stock_on_warehouse = asyncio.create_task(supplier.get_analytics_stock_on_warehouse(
    #     limit = 100,
    #     offset = 0
    # ))

    # print((await analytics_stock_on_warehouse))

    # product_info_list = asyncio.create_task(supplier.get_product_info_list(

    #        product_id=[247465013],

    # ))

    # print((await product_info_list))

    category_tree = asyncio.create_task(supplier.get_category_tree(

           category_id=17028968

    ))

    print((await category_tree))

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

