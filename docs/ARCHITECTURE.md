# SPAM Network Architecture

> Version: 1.0 (Foundation)
> Status: In Development

---

# Table of Contents

- Project Vision
- Design Principles
- High-Level Architecture
- Project Structure
- Technology Stack
- Backend Architecture
- Telegram Architecture
- Database
- Security
- AI Layer
- Token Economy
- Scalability
- Development Standards

---

# Project Vision

SPAM (Social Pump Anonymous Market) — анонимная социальная сеть нового поколения для экосистемы мемкоинов, ориентированная на пользователей Pump.fun, трейдеров и криптосообщества.

Основные принципы:

- отсутствие публичной идентификации пользователя;
- отсутствие хранения чувствительных персональных данных;
- многоязычная коммуникация с автоматическим переводом;
- модульная архитектура;
- горизонтальная масштабируемость.

---

# Design Principles

Проект строится согласно следующим принципам:

- Clean Architecture
- SOLID
- DRY
- KISS
- Explicit over Implicit
- Security First
- Privacy by Design

---

# High-Level Architecture

```
Telegram
     │
     ▼
Aiogram
     │
     ▼
Middleware
     │
     ▼
Handlers
     │
     ▼
Services
     │
     ▼
Repositories
     │
     ▼
PostgreSQL
```

Дополнительные сервисы:

- Redis
- AI Translation
- Moderation Engine
- Analytics
- Token Economy

---

# Project Structure

```
SPAM/

backend/
    app/
        api/
        bot/
        core/
        database/
        identity/
        middleware/
        models/
        repositories/
        schemas/
        services/
        translations/

    migrations/
    tests/

docs/

docker/

.github/
```

---

# Technology Stack

## Backend

- Python 3.14
- FastAPI
- SQLAlchemy 2.x
- Alembic
- aiogram 3.x

## Database

- PostgreSQL 16
- Redis

## DevOps

- Docker
- Docker Compose
- GitHub Actions

## Code Quality

- Ruff
- pytest
- mypy
- pre-commit

---

# Backend Architecture

Структура Backend:

API

↓

Services

↓

Repositories

↓

Database

Слой Repository никогда не содержит бизнес-логики.

Бизнес-логика располагается исключительно в Services.

---

# Telegram Architecture

Bot

↓

Dispatcher

↓

Router

↓

Middleware

↓

Handlers

↓

Services

Каждый Handler отвечает только за взаимодействие с Telegram API.

---

# Database

Основные таблицы:

users

anonymous_profiles

tripcodes

messages

rooms

languages

announcements

ranks

reports

moderation_logs

economy

transactions

staking

---

# Security

Основные требования:

- отсутствие хранения Telegram ID в открытом виде;
- SHA-256/BLAKE3 хэширование внутренних идентификаторов;
- безопасная работа с токенами;
- обязательное использование переменных окружения;
- минимизация собираемых данных.

---

# AI Layer

Будущие компоненты:

- AI Translation
- AI Moderation
- AI Spam Detection
- AI Topic Classification
- AI Semantic Search

---

# Token Economy

Планируемые возможности:

- Premium Rank
- Paid Announcements
- DAO Governance
- SPAM Utility
- Staking
- Reputation

---

# Scalability

Архитектура проектируется под возможность:

- разделения сервисов;
- микросервисного перехода;
- горизонтального масштабирования;
- нескольких Telegram-инстансов.

---

# Development Standards

Каждый этап разработки должен включать:

- документацию;
- тестирование;
- Git checkpoint;
- обновление CHANGELOG;
- обновление ROADMAP.

Без выполнения этих пунктов этап считается незавершённым.
