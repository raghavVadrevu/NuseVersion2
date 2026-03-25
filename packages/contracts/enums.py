from __future__ import annotations

from enum import Enum


class SourceType(str, Enum):
    RSS = "RSS"
    GOOGLE_NEWS = "GOOGLE_NEWS"
    WEB = "WEB"


class DocumentStatus(str, Enum):
    DISCOVERED = "DISCOVERED"
    ACQUIRED = "ACQUIRED"
    EXTRACTED = "EXTRACTED"
    PROCESSED = "PROCESSED"
    CHUNKED = "CHUNKED"
    INDEXED = "INDEXED"
    FAILED = "FAILED"


class ContentLanguage(str, Enum):
    EN = "EN"


class Category(str, Enum):
    WORLD = "WORLD"
    INDIA = "INDIA"
    BUSINESS = "BUSINESS"
    TECHNOLOGY = "TECHNOLOGY"
    SPORTS = "SPORTS"
    ENTERTAINMENT = "ENTERTAINMENT"
    GENERAL = "GENERAL"
