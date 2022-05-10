from .base import BaseRequest
from pydantic import Field
from enum import Enum
from rfc3339_validator import validate_rfc3339
from pydantic import validator

class Status(str, Enum):
    empty = ''
    awaiting_registration = 'awaiting_registration'
    acceptance_in_progress = 'acceptance_in_progress'
    awaiting_approve = 'awaiting_approve'
    awaiting_packaging = 'awaiting_packaging'
    awaiting_deliver = 'awaiting_deliver'
    arbitration = 'arbitration'
    client_arbitration = 'client_arbitration'
    delivering = 'delivering'
    driver_pickup = 'driver_pickup'
    delivered = 'delivered'
    cancelled = 'cancelled'
    not_accepted = 'not_accepted'

class PostingFBSListFilter(BaseRequest):
    delivery_method_id: list[int]
    order_id: int
    provider_id: list[int]
    since: str
    to: str
    status: Status
    warehouse_id: list[int]

    @validator('since')
    def validate_since(cls, v):
        if not validate_rfc3339(v):
            raise ValueError("date_start must be rfc3339 valid")
        return v

    @validator('to')
    def validate_to(cls, v):
        if not validate_rfc3339(v):
            raise ValueError("date_start must be rfc3339 valid")
        return v

class PostingFBSListWith(BaseRequest):
    analytics_data: bool
    barcodes: bool
    financial_data: bool
    translit: bool

class PostingFBSListRequest(BaseRequest):
    dir: str
    filter: PostingFBSListFilter
    limit: int
    offset: int
    with_field: PostingFBSListWith = Field(None, alias='with')