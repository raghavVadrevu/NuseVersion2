from __future__ import annotations

from typing import Dict, List

from pydantic import BaseSettings

from packages.contracts.enums import Category


class Settings(BaseSettings):
    RABBITMQ_HOST: str = "rabbitmq"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USERNAME: str = "guest"
    RABBITMQ_PASSWORD: str = "guest"
    RABBITMQ_EXCHANGE: str = "nuse.events"
    RABBITMQ_QUEUE: str = "article_discovered"
    RABBITMQ_ROUTING_KEY: str = "article.discovered"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


FEED_MAP: Dict[Category, List[str]] = {
    Category.WORLD: [
        "http://feeds.bbci.co.uk/news/world/rss.xml",
    ],
    Category.INDIA: [
        "https://www.thehindu.com/news/national/feeder/default.rss",
    ],
    Category.BUSINESS: [
        "https://www.cnbc.com/id/10001147/device/rss/rss.html",
    ],
    Category.TECHNOLOGY: [
        "http://feeds.feedburner.com/TechCrunch/",
    ],
    Category.SPORTS: [
        "https://www.espn.com/espn/rss/news",
    ],
    Category.ENTERTAINMENT: [
        "https://feeds.feedburner.com/entertainment-weekly/latest",
    ],
}
