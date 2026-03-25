from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ..base import BaseEvent
from ..enums import DocumentStatus


class DocumentAcquiredEvent(BaseEvent):
    doc_id: str
    url: str
    canonical_url: Optional[str] = None
    source_name: str
    raw_html_path: Optional[str] = None
    fetched_at: datetime
    status: DocumentStatus
