from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from uuid import uuid4

import feedparser

from packages.contracts.enums import Category, SourceType
from packages.contracts.events.article_discovered import ArticleDiscoveredEvent
from config import FEED_MAP


def discover_articles(
    category: Optional[Category] = None,
) -> Tuple[Dict[str, int], List[ArticleDiscoveredEvent]]:
    total_feeds_checked = 0
    total_entries_seen = 0
    events: List[ArticleDiscoveredEvent] = []
    seen_links = set()

    categories = [category] if category is not None else list(FEED_MAP.keys())

    for cat in categories:
        feeds = FEED_MAP.get(cat, [])

        for feed_url in feeds:
            parsed = feedparser.parse(feed_url)
            total_feeds_checked += 1

            feed_title = getattr(parsed.feed, "title", None) or "Unknown Source"
            entries = parsed.entries or []
            total_entries_seen += len(entries)

            for entry in entries:
                link = getattr(entry, "link", None)
                if not link or link in seen_links:
                    continue

                seen_links.add(link)
                now = datetime.now(timezone.utc)

                event = ArticleDiscoveredEvent(
                    event_id=str(uuid4()),
                    event_type="article.discovered",
                    emitted_at=now,
                    trace_id=None,
                    source_type=SourceType.RSS,
                    source_name=feed_title,
                    url=link,
                    discovered_at=now,
                    category=cat,
                )
                events.append(event)

    stats = {
        "total_feeds_checked": total_feeds_checked,
        "total_entries_seen": total_entries_seen,
        "total_events_published": len(events),
    }

    return stats, events