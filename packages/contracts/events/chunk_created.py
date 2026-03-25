from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ..base import BaseEvent
from ..enums import Category


class ChunkCreatedEvent(BaseEvent):
    chunk_id: str
    doc_id: str
    position: int
    content: str
    token_count: int
    title: str
    source_name: str
    url: str
    category: Category
    published_at: Optional[datetime] = None
