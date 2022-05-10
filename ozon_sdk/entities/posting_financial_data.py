from .base import BaseEntity

class PostingFinancialDataServices(BaseEntity):
    marketplace_service_item_deliv_to_customer: float
    marketplace_service_item_direct_flow_trans: float
    marketplace_service_item_dropoff_ff: float
    marketplace_service_item_dropoff_pvz: float
    marketplace_service_item_dropoff_sc: float
    marketplace_service_item_fulfillment: float
    marketplace_service_item_pickup: float
    marketplace_service_item_return_after_deliv_to_customer: float
    marketplace_service_item_return_flow_trans: float
    marketplace_service_item_return_not_deliv_to_customer: float
    marketplace_service_item_return_part_goods_customer: float

class ProductPicking(BaseEntity):
    amount: float
    moment: str
    tag: str

class PostingFinancialDataProduct(BaseEntity):
    actions: list[str]
    client_price: str
    commission_amount: float
    commission_percent: int
    item_services: PostingFinancialDataServices
    old_price: float
    payout: float
    picking: None
    price: float
    product_id: int
    quantity: int
    total_discount_percent: float
    total_discount_value: float

class FinacialData(BaseEntity):
    posting_services: PostingFinancialDataServices
    products: list[ProductPicking]