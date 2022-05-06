from datetime import datetime
from .base import BaseEntity
from .itemerror import ItemError

class Status(BaseEntity):
    state: str
    state_failed: str
    moderate_status: str
    decline_reasons: list[str]
    validation_state: str
    state_name: str
    state_description: str
    is_failed: bool
    is_created: bool
    state_tooltip: str
    item_errors: list[ItemError]
    state_updated_at: datetime
