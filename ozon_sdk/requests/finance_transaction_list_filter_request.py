from pydantic import Field
from .base import BaseRequest
from enum import Enum

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

class FinanceTransactionListV3RequestFilter(BaseRequest):
    date: Date
    operation_type: list[OperationTypeEnum]
    posting_number: str
    transaction_type: TransactionTypeEnum