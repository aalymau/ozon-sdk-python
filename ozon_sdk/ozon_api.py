from .get_product_info import OzonMethods
from .ozonfbsfbo import OzonFboFbs
from .ozon_transaction import OzonTransaction

class OzonApi(OzonMethods, OzonFboFbs, OzonTransaction):
    """_summary_

    Args:
        OzonMethods (_type_): _description_
        OzonFboFbs (_type_): _description_
        OzonTransaction (_type_): _description_
    """
