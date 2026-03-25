from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from ..base import BaseEvent
from ..enums import Category, SourceType


class ArticleDiscoveredEvent(BaseEvent):
    source_type: SourceType
    source_name: str
    url: str
    discovered_at: datetime
    category: Category
