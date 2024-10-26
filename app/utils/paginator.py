from typing import TypeVar, Generic, List, Dict
from dataclasses import dataclass
from sqlalchemy.orm import Query
import math

T = TypeVar('T')

@dataclass
class PaginationMeta:
    total: int
    last_page: int
    current_page: int
    page_size: int
    prev: int | None
    next: int | None

@dataclass
class PagedResponse(Generic[T]):
    data: List[T]
    meta: PaginationMeta

@dataclass
class QueryResult(Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int

class Paginator:
    @staticmethod
    def paginate_query(query: Query, page: int, page_size: int) -> QueryResult[T]:
        total = query.count()
        items = query.offset((page - 1) * page_size).limit(page_size).all()
        return QueryResult(
            items=items,
            total=total,
            page=page,
            page_size=page_size
        )

    @staticmethod
    def paginate(result: QueryResult[T]) -> PagedResponse[T]:
        last_page = math.ceil(result.total / result.page_size)

        meta = PaginationMeta(
            total=result.total,
            last_page=last_page,
            current_page=result.page,
            page_size=result.page_size,
            prev=result.page - 1 if result.page > 1 else None,
            next=result.page + 1 if result.page < last_page else None
        )

        return PagedResponse(
            data=result.items,
            meta=meta
        )
