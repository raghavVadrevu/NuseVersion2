from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from ..base import BaseEvent
from ..enums import Category, ContentLanguage, DocumentStatus


class DocumentProcessedEvent(BaseEvent):
    doc_id: str
    url: str
    source_name: str
    title: str
    cleaned_text: str
    language: ContentLanguage
    category: Category
    quality_score: float
    dedup_cluster_id: Optional[str] = None
    status: DocumentStatus
