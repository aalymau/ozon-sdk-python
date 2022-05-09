from .base import BaseEntity
from typing import List

class CategoryTree(BaseEntity):
    """Дерево категории товаров"""

    category_id: int
    children: List['CategoryTree'] = []
    title: str