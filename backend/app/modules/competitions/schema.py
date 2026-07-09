# Principle: API schemas are separate from database models. This prevents exposing database internals directly.
import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.common.enums import Sport


class CompetitionBase(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Competition name",
    )

    country: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Country where the competition is held",
    )

    sport: Sport = Field(
        ...,
        description="Sport type",
    )

    season: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Competition season",
    )


class CompetitionCreate(CompetitionBase):
    pass


class CompetitionUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100,
        description="Competition name",
    )

    country: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Country where the competition is held",
    )

    sport: Optional[Sport] = Field(
        default=None,
        description="Sport type",
    )

    season: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Competition season",
    )


class CompetitionResponse(CompetitionBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True