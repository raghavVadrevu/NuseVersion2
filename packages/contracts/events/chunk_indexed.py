from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from ..base import BaseEvent
from ..enums import DocumentStatus


class ChunkIndexedEvent(BaseEvent):
    chunk_id: str
    doc_id: str
    vector_id: str
    indexed_at: datetime
    status: DocumentStatus
