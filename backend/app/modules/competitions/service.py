# Principle: Service Layer. The service owns business logic and validation, while the repository only talks to the database.
import uuid

from fastapi import HTTPException, status

from app.modules.competitions.repository import CompetitionRepository
from app.modules.competitions.schema import CompetitionCreate, CompetitionUpdate, CompetitionResponse
from math import ceil
from typing import Optional

from app.common.schemas import PaginatedResponse



class CompetitionService:
    def __init__(self, repository: CompetitionRepository):
        self.repository = repository

    def list_competitions(
        self,
        page: int,
        page_size: int,
        sport: Optional[str] = None,
        country: Optional[str] = None,
    ) -> PaginatedResponse[CompetitionResponse]:
        # Repository returns current page items and total matching records.
        items, total = self.repository.list(
            page=page,
            page_size=page_size,
            sport=sport,
            country=country,
        )

        # Calculate total pages for frontend pagination controls.
        total_pages = ceil(total / page_size) if total > 0 else 0

        return PaginatedResponse(
            items=items,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )
    def get_competition(self, competition_id: uuid.UUID):
        competition = self.repository.get_by_id(competition_id)

        if competition is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Competition not found",
            )

        return competition

    def create_competition(self, payload: CompetitionCreate):
        return self.repository.create(payload)

    def update_competition(self, competition_id: uuid.UUID, payload: CompetitionUpdate):
        competition = self.get_competition(competition_id)
        return self.repository.update(competition, payload)

    def delete_competition(self, competition_id: uuid.UUID):
        competition = self.get_competition(competition_id)
        self.repository.delete(competition)
        return None