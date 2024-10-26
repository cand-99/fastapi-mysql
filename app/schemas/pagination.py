from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class PageParams(BaseModel):
    page: int = 1
    page_size: int = 10

class PaginationMeta(BaseModel):
    total: int
    last_page: int
    current_page: int
    page_size: int
    prev: Optional[int]
    next: Optional[int]

class PagedResponse(BaseModel, Generic[T]):
    data: List[T]
    meta: PaginationMeta
    
