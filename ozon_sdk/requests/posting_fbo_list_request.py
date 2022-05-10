from pydantic import validator
from .base import BaseRequest
from pydantic import Field
from enum import Enum

class StatusEnum(str, Enum):
    empty = ''
    awaiting_packaging = 'awaiting_packaging'
    awaiting_deliver = 'awaiting_deliver'
    delivering = 'delivering'
    delivered = 'delivered'
    cancelled = 'cancelled'

class PostingFBOListFilter(BaseRequest):
    since: str
    status: StatusEnum
    to: str

class PostingFBOListWith(BaseRequest):
    analytics_data: bool
    financial_data: bool

class PostingFBOListRequest(BaseRequest):
    """Список отправлений"""
    dir: str
    filter: PostingFBOListFilter
    limit: int
    offset: int
    translit: bool
    with_field: PostingFBOListWith = Field(None, alias='with')

    @validator('limit')
    def validate_limit(cls, v):
        if v > 1000:
            return 1000
        if v < 1:
            return 1
        return v