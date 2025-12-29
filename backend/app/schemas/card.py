from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.enums import CardType


class CardBase(BaseModel):
    type: CardType = CardType.BASIC
    prompt: str
    answer: str
    explanation: Optional[str] = None


class CardCreate(CardBase):
    pass


class CardUpdate(BaseModel):
    type: Optional[CardType] = None
    prompt: Optional[str] = None
    answer: Optional[str] = None
    explanation: Optional[str] = None


class CardRead(CardBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    deck_id: int
    created_at: datetime
    updated_at: datetime

