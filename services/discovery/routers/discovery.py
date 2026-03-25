from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from packages.contracts.api.headlines import HeadlinesResponse  # optional to remove later
from packages.contracts.enums import Category
from services.feed_service import discover_articles
from services.publisher import EventPublisher

router = APIRouter(tags=["discovery"])


class DiscoverRequest(BaseModel):
    category: Optional[Category] = None


@router.post("/discover")
def discover(payload: DiscoverRequest):
    stats, events = discover_articles(payload.category)

    publisher = EventPublisher()
    published_count = publisher.publish_article_discovered_events(events)

    return {
        "total_feeds_checked": stats["total_feeds_checked"],
        "total_entries_seen": stats["total_entries_seen"],
        "total_events_published": published_count,
        "category_filter": payload.category.value if payload.category else None,
    }