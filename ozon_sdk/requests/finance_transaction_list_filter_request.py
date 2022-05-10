from pydantic import Field
from .base import BaseRequest
from enum import Enum
from rfc3339_validator import validate_rfc3339
from pydantic import validator

class OperationTypeEnum(str, Enum):
    ClientReturnAgentOperation = 'ClientReturnAgentOperation'
    MarketplaceMarketingActionCostOperation = 'MarketplaceMarketingActionCostOperation'
    MarketplaceSaleReviewsOperation = 'MarketplaceSaleReviewsOperation'
    MarketplaceSellerCompensationOperation = 'MarketplaceSellerCompensationOperation'
    OperationAgentDeliveredToCustomer = 'OperationAgentDeliveredToCustomer' 
    OperationAgentDeliveredToCustomerCanceled = 'OperationAgentDeliveredToCustomerCanceled'
    OperationAgentStornoDeliveredToCustomer = 'OperationAgentStornoDeliveredToCustomer'
    OperationClaim = 'OperationClaim'
    OperationCorrectionSeller = 'OperationCorrectionSeller'
    OperationDefectiveWriteOff = 'OperationDefectiveWriteOff'
    OperationItemReturn = 'OperationItemReturn'
    OperationLackWriteOff = 'OperationLackWriteOff'
    OperationMarketplaceCrossDockServiceWriteOff = 'OperationMarketplaceCrossDockServiceWriteOff'
    OperationMarketplaceServiceStorage = 'OperationMarketplaceServiceStorage'
    OperationSetOff = 'OperationSetOff'
    MarketplaceSellerReexposureDeliveryReturnOperation = 'MarketplaceSellerReexposureDeliveryReturnOperation' 
    OperationReturnGoodsFBSofRMS = 'OperationReturnGoodsFBSofRMS' 
    ReturnAgentOperationRFBS = 'ReturnAgentOperationRFBS'
    MarketplaceSellerShippingCompensationReturnOperation = 'MarketplaceSellerShippingCompensationReturnOperation'
    OperationMarketplaceServicePremiumCashback = 'OperationMarketplaceServicePremiumCashback'

class TransactionTypeEnum(str, Enum):
    all = 'all'
    orders = 'orders'
    returns  = 'returns'
    services = 'services'
    compensation = 'compensation'
    transferDelivery = 'transferDelivery'
    other = 'other'

class Date(BaseRequest):
    from_field: str = Field(None, alias='from')
    to: str

    @validator('from_field')
    def validate_from_field(cls, v):
        if not validate_rfc3339(v):
            raise ValueError("date_start must be rfc3339 valid")
        return v

    @validator('to')
    def validate_to(cls, v):
        if not validate_rfc3339(v):
            raise ValueError("date_start must be rfc3339 valid")
        return v

class FinanceTransactionListV3RequestFilter(BaseRequest):
    date: Date
    operation_type: list[OperationTypeEnum]
    posting_number: str
    transaction_type: TransactionTypeEnum