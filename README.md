# NUSEVERSION2

This repository contains a microservices-based Retrieval-Augmented Generation (RAG) system.

## Architecture Overview

- **Services**: Each domain-specific service (gateway, discovery, acquisition, extraction, processing, chunking, indexing, retrieval, reranking, generation) is implemented as an independent FastAPI app with a `/health` endpoint and its own Dockerfile.
- **Packages**: Shared Python packages (`contracts`, `common`, `config`, `logging`, `clients`) provide common models, utilities, configuration, logging, and client abstractions to keep services lightweight and consistent.
- **Infrastructure**: The `infra` directory holds configuration for core dependencies such as RabbitMQ, Postgres, Redis, and Qdrant, as well as `compose` for higher-level orchestration.
- **Docs**: The `docs` directory is reserved for architecture diagrams, ADRs, and other project documentation.

The root-level `docker-compose.yml` will orchestrate all services and infrastructure components to run the full RAG stack locally.