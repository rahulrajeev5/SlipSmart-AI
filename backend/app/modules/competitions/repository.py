# Principle: Repository Pattern. This keeps database queries out of routers and services.
import uuid
from typing import Optional

from sqlalchemy.orm import Session

from app.modules.competitions.model import Competition
from app.modules.competitions.schema import CompetitionCreate, CompetitionUpdate


class CompetitionRepository:
    def __init__(self, db: Session):
        self.db = db

# Principle: Repository Pattern
# Responsibility: Only communicate with the database.
# No HTTP logic.
# No business logic.

    def list(
        self,
        page: int,
        page_size: int,
        sport: Optional[str] = None,
        country: Optional[str] = None,
    ) -> tuple[list[Competition], int]:
        # Pagination offset.
        offset = (page - 1) * page_size

        # Start query. SQL is not executed yet.
        query = self.db.query(Competition)

        # Filter by sport if provided.
        if sport:
            query = query.filter(Competition.sport == sport)

        if country:
            query = query.filter(Competition.country == country)

        # Count total records after filters.
        total = query.count()

        # Fetch only current page records.
        items = (
            query.order_by(Competition.created_at.desc())
            .offset(offset)
            .limit(page_size)
            .all()
        )

        return items, total
            
    def get_by_id(self, competition_id: uuid.UUID) -> Optional[Competition]:
            return (
                self.db.query(Competition)
                .filter(Competition.id == competition_id)
                .first()
            )

    def create(self, payload: CompetitionCreate) -> Competition:
        competition = Competition(**payload.model_dump())
        self.db.add(competition)
        self.db.commit()
        self.db.refresh(competition)
        return competition

    def update(
        self,
        competition: Competition,
        payload: CompetitionUpdate,
    ) -> Competition:
        update_data = payload.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(competition, key, value)

        self.db.commit()
        self.db.refresh(competition)
        return competition

    def delete(self, competition: Competition) -> None:
        self.db.delete(competition)
        self.db.commit()