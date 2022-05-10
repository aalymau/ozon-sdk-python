from .base import BaseEntity
from .fbs_posting import FBSPosting

class PostingFBSList(BaseEntity):
    has_next: bool
    postings: list[FBSPosting]