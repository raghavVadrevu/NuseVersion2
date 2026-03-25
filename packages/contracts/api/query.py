from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

from ..enums import Category


class QueryRequest(BaseModel):
    query: str
    category: Optional[Category] = None
    top_k: int = 8


class Citation(BaseModel):
    doc_id: str
    chunk_id: str
    title: str
    source_name: str
    url: str


class QueryResponse(BaseModel):
    query: str
    answer: str
    citations: List[Citation]
