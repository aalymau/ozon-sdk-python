from .base import BaseResponse
from ..entities import CategoryTree

class CategoryTreeResponse(BaseResponse):
    result: list[CategoryTree]