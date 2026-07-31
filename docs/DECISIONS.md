# SPAM Network — Architecture Decision Records (ADR)

> Version: 1.0
> Status: Active
> Last Updated: 2026-07-31

---

# Table of Contents

- About ADR
- ADR-001 — Project Philosophy
- ADR-002 — Backend Framework
- ADR-003 — Programming Language
- ADR-004 — Dependency Management
- ADR-005 — Database
- ADR-006 — SQLAlchemy Strategy
- ADR-007 — Alembic Strategy
- ADR-008 — Telegram Framework
- ADR-009 — Anonymous Identity
- ADR-010 — Repository Structure
- ADR-011 — Security Principles
- ADR-012 — AI Integration
- ADR-013 — Documentation Policy
- ADR-014 — Testing Policy
- Future ADRs

---

# About ADR

Architecture Decision Records (ADR) фиксируют все ключевые инженерные решения проекта.

Каждый ADR содержит:

- проблему;
- принятое решение;
- причину выбора;
- последствия;
- возможные альтернативы.

После принятия ADR считается частью архитектуры проекта.

Изменение ADR допускается только при наличии объективных технических причин.

---

# ADR-001 — Project Philosophy

## Status

Accepted

## Decision

SPAM строится как долгоживущая платформа, а не MVP.

## Reason

Стоимость ранних архитектурных решений значительно ниже стоимости рефакторинга после запуска.

## Consequences

- допускается более медленная разработка;
- запрещены временные "костыли";
- каждый компонент должен быть масштабируемым.

---

# ADR-002 — Backend Framework

## Status

Accepted

## Decision

Использовать FastAPI.

## Reason

- современный ASGI;
- высокая производительность;
- строгая типизация;
- отличная интеграция с SQLAlchemy;
- активная экосистема.

## Alternatives

- Django
- Flask
- Litestar

---

# ADR-003 — Programming Language

## Status

Accepted

## Decision

Python 3.14

## Reason

- современный синтаксис;
- развитая экосистема;
- высокая скорость разработки;
- совместимость с AI-библиотеками.

## Notes

При возникновении несовместимости библиотек допускается временный переход на Python 3.13 до стабилизации экосистемы.

---

# ADR-004 — Dependency Management

## Status

Accepted

## Decision

Использовать uv и pyproject.toml.

## Reason

- высокая скорость;
- единая спецификация проекта;
- современный стандарт Python.

## Deprecated

requirements.txt не используется как основной источник зависимостей.

---

# ADR-005 — Database

## Status

Accepted

## Decision

Основная база данных — PostgreSQL.

Redis используется только как вспомогательный сервис.

## Reason

PostgreSQL обеспечивает:

- ACID;
- расширяемость;
- JSONB;
- полнотекстовый поиск;
- зрелую экосистему.

---

# ADR-006 — SQLAlchemy Strategy

## Status

Accepted

## Decision

Приложение использует асинхронный SQLAlchemy.

## Reason

Telegram-бот работает в асинхронной среде.

Используется:

- Async Engine
- Async Session

---

# ADR-007 — Alembic Strategy

## Status

Accepted

## Decision

Alembic использует синхронное подключение к PostgreSQL.

## Reason

Это официально рекомендуемая практика.

## Consequences

Используются два URL:

DATABASE_ASYNC_URL

DATABASE_SYNC_URL

---

# ADR-008 — Telegram Framework

## Status

Accepted

## Decision

Использовать aiogram 3.x.

## Reason

- Router API;
- Middleware;
- FSM;
- современная архитектура;
- поддержка Telegram Bot API.

---

# ADR-009 — Anonymous Identity

## Status

Accepted

## Decision

Telegram ID не используется как публичный идентификатор.

Для внутренней логики создаётся уникальный SPAM Hash.

## Principles

Запрещено:

- отображать Telegram ID;
- использовать username как основной идентификатор;
- раскрывать внутренние идентификаторы.

## Planned

SPAM Hash

↓

Anonymous Profile

↓

Tripcode

---

# ADR-010 — Repository Structure

## Status

Accepted

## Decision

Проект использует модульную архитектуру.

```
backend/

app/

core/

database/

bot/

services/

repositories/

models/

schemas/

middleware/

tests/
```

Каждый модуль отвечает только за свою область.

---

# ADR-011 — Security Principles

## Status

Accepted

## Decision

Проект следует принципу Privacy by Design.

### Основные правила

Минимизировать сбор данных.

Не хранить чувствительные данные без необходимости.

Использовать переменные окружения.

Разделять публичные и внутренние идентификаторы.

Проводить проверку входных данных.

Использовать параметризованные SQL-запросы через ORM.

---

# ADR-012 — AI Integration

## Status

Accepted

## Decision

Все AI-компоненты реализуются как отдельный сервисный слой.

Планируемые сервисы:

- Translation Engine
- Moderation Engine
- Spam Detection
- Topic Classification
- Semantic Search

---

# ADR-013 — Documentation Policy

## Status

Accepted

## Decision

Каждый завершённый этап обязан сопровождаться обновлением документации.

Обновляются:

- README.md
- ARCHITECTURE.md
- ROADMAP.md
- CHANGELOG.md
- DECISIONS.md

Без этого этап считается незавершённым.

---

# ADR-014 — Testing Policy

## Status

Accepted

## Decision

Каждый новый модуль проходит обязательную проверку.

Минимальный набор:

- локальный запуск;
- проверка линтеров;
- тесты;
- миграции (если применимо).

После успешной проверки выполняется Git checkpoint.

---

# Future ADRs

Планируется добавить решения по следующим темам:

- Encryption Strategy
- SPAM Hash Algorithm
- Tripcode Specification
- Reputation Algorithm
- Rank System
- Economy Engine
- DAO Governance
- AI Translation Providers
- Moderation Policy
- Internationalization (i18n)
- Plugin Architecture
- API Versioning
- Event Bus
- Redis Strategy
- Background Workers
- Rate Limiting
- Caching
- Logging Strategy
- Monitoring
- CI/CD
- Production Deployment

---

# ADR Lifecycle

Каждый ADR проходит следующие стадии:

Proposed

↓

Review

↓

Accepted

↓

Implemented

↓

Deprecated (при необходимости)

---

> **Основной принцип проекта SPAM:**
>
> **"Любое архитектурное решение принимается один раз, документируется, проверяется и становится частью инженерной базы проекта."**
