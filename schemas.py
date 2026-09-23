from pydantic import BaseModel
from typing import Optional


class StylistRequest(BaseModel):

    destination: Optional[str] = None

    occasion: Optional[str] = None

    body_type: Optional[str] = None

    undertone: Optional[str] = None

    style: Optional[str] = None

    budget_min: Optional[float] = None

    budget_max: Optional[float] = None

    query: Optional[str] = None