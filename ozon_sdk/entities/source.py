from .base import BaseEntity

class Source(BaseEntity):
    is_enabled: bool
    sku: int
    source: str