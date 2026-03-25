from datetime import datetime, UTC
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel

from packages.contracts.enums import Category, SourceType
from packages.contracts.events.article_discovered import ArticleDiscoveredEvent
from services.feed_service import FeedDiscoveryService
from services.publisher import RabbitMQPublisher

router = APIRouter(tags=["discovery"])


class DiscoverRequest(BaseModel):
    category: Optional[Category] = None


@router.post("/discover")
def discover(payload: DiscoverRequest):
    feed_service = FeedDiscoveryService()
    publisher = RabbitMQPublisher()

    feeds = feed_service.get_feed_urls(
        payload.category.value if payload.category else None
    )
    discovered, total_entries_seen = feed_service.fetch_entries(
        payload.category.value if payload.category else None
    )

    total_events_published = 0
    total_feeds_checked = sum(len(urls) for urls in feeds.values())

    try:
        publisher.connect()

        for item in discovered:
            event = ArticleDiscoveredEvent(
                event_id=str(uuid4()),
                event_type="article.discovered",
                emitted_at=datetime.now(UTC),
                trace_id=None,
                source_type=SourceType.RSS,
                source_name=item["source_name"],
                url=item["url"],
                discovered_at=datetime.now(UTC),
                category=Category[item["category"]],
            )

            publisher.publish(event.model_dump(mode="json"))
            total_events_published += 1

    finally:
        publisher.close()

    return {
        "total_feeds_checked": total_feeds_checked,
        "total_entries_seen": total_entries_seen,
        "total_events_published": total_events_published,
        "category_filter": payload.category.value if payload.category else None,
    }