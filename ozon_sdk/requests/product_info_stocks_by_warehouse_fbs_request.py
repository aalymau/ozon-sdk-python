from .base import BaseRequest
from pydantic import validator

class ProductInfoStocksByWarehouseFBSRequest(BaseRequest):
    fbs_sku: list[str]

    @validator('fbs_sku')
    def validate_fbs_sku_length(cls, v):
        if len(v) > 500:
            raise ValueError('Слишком много sku, нельзя больше 500 значений за раз')
        return v