from lib2to3.pytree import Base
from .base import BaseEntity
from .posting_financial_data import FinacialData
from .fbs_posting_analytics_data import FPSPostingAnalyticsData
from .customer import Customer
from .fbs_posting_product import FBSPostingProduct
from .fbs_posting_requirements import FBSPostingRequirements
from datetime import datetime

class Addressee(BaseEntity):
    name: str
    phone: str

class Barcodes(BaseEntity):
    lower_barcode: str
    upper_barcode: str

class Cancellation(BaseEntity):
    affect_cancellation_rating: bool
    cancel_reason: str
    cancel_reason_id: int
    cancellation_initiator: str
    cancellation_type: str
    cancelled_after_ship: bool

class DeliveryMethod(BaseEntity):
    id: int
    name: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int

class FBSPosting(BaseEntity):
    addressee: Addressee
    analytics_data: FPSPostingAnalyticsData
    barcodes: Barcodes
    cancellation: Cancellation
    customer: Customer
    delivering_date: datetime
    delivery_method: DeliveryMethod
    financial_data: FinacialData
    in_process_at: str
    is_express: bool
    order_id: int
    order_number: str
    posting_number: str
    products: list[FBSPostingProduct]
    requirements: FBSPostingRequirements
    shipment_date: datetime
    status: str
    tpl_integration_type: str
    tracking_number: str