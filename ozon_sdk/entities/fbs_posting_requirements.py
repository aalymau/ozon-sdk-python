from .base import BaseEntity

class FBSPostingRequirements(BaseEntity):
    products_requiring_gtd: list[str]
    products_requiring_country: list[str]
    products_requiring_mandatory_mark: list[str]