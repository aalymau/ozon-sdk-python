from .base import BaseRequest
from enum import Enum

class Language(str, Enum):
    DEFAULT = 'DEFAULT'
    RU = 'RU'
    EN = 'EN'

class CategoryTreeRequest(BaseRequest):
    """Дерево категории товаров"""
    
    category_id: int
    language: Language
