from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

from ..enums import Category


class HeadlinesRequest(BaseModel):
    category: Optional[Category] = None
    limit: int = 5


class HeadlineItem(BaseModel):
    rank: int
    title: str
    source_name: Optional[str] = None
    url: Optional[str] = None


class HeadlinesResponse(BaseModel):
    category: Optional[Category] = None
    headlines: List[HeadlineItem]
