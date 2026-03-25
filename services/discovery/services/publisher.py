from __future__ import annotations

from typing import Iterable

import pika

from packages.contracts.events.article_discovered import ArticleDiscoveredEvent
from config import Settings


class EventPublisher:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings()

    def _connection_parameters(self) -> pika.ConnectionParameters:
        credentials = pika.PlainCredentials(
            self.settings.RABBITMQ_USERNAME,
            self.settings.RABBITMQ_PASSWORD,
        )
        return pika.ConnectionParameters(
            host=self.settings.RABBITMQ_HOST,
            port=self.settings.RABBITMQ_PORT,
            credentials=credentials,
        )

    def publish_article_discovered_events(
        self, events: Iterable[ArticleDiscoveredEvent]
    ) -> int:
        params = self._connection_parameters()
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.exchange_declare(
            exchange=self.settings.RABBITMQ_EXCHANGE,
            exchange_type="direct",
            durable=True,
        )
        channel.queue_declare(
            queue=self.settings.RABBITMQ_QUEUE,
            durable=True,
        )
        channel.queue_bind(
            exchange=self.settings.RABBITMQ_EXCHANGE,
            queue=self.settings.RABBITMQ_QUEUE,
            routing_key=self.settings.RABBITMQ_ROUTING_KEY,
        )

        published_count = 0
        for event in events:
            body = event.json()
            channel.basic_publish(
                exchange=self.settings.RABBITMQ_EXCHANGE,
                routing_key=self.settings.RABBITMQ_ROUTING_KEY,
                body=body,
                properties=pika.BasicProperties(
                    content_type="application/json",
                    delivery_mode=2,
                ),
            )
            published_count += 1

        connection.close()
        return published_count