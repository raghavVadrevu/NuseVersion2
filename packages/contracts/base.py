from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseEvent(BaseModel):
    event_id: str
    event_type: str
    event_version: str = "v1"
    emitted_at: datetime
    trace_id: Optional[str] = None
