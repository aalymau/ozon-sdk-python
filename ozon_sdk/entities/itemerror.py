from .base import BaseEntity

class OptionalDescriptionElements(BaseEntity):
    property_name: str

class ItemError(BaseEntity):
    code: str
    state: str
    level: str
    description: str
    field: str
    attribute_id: int
    attribute_name: str
    optional_description_elements: OptionalDescriptionElements