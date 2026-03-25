from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ..base import BaseEvent
from ..enums import DocumentStatus


class DocumentExtractedEvent(BaseEvent):
    doc_id: str
    url: str
    canonical_url: Optional[str] = None
    source_name: str
    title: str
    author: Optional[str] = None
    published_at: Optional[datetime] = None
    extracted_text: str
    status: DocumentStatus
