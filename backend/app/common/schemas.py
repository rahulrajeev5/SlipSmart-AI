from typing import Generic, TypeVar

from pydantic import BaseModel

# Generic type.
# T can represent CompetitionResponse, TeamResponse, MatchResponse, etc.
T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    # Actual records returned by the API.
    items: list[T]

    # Total number of records in the database after filters.
    total: int

    # Current page requested by the client.
    page: int

    # Number of records returned per page.
    page_size: int

    # Total number of available pages.
    total_pages: int