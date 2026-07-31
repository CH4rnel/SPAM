# SPAM Network Coding Standard

> Version: 1.0
> Status: Active
> Last Updated: 2026-07-31

---

# Table of Contents

1. Purpose
2. Engineering Principles
3. Project Structure
4. Python Style Guide
5. Naming Conventions
6. Module Organization
7. Database Standards
8. API Standards
9. Telegram Bot Standards
10. Error Handling
11. Logging
12. Security
13. Configuration
14. Testing
15. Git Workflow
16. Documentation
17. Performance
18. Code Review Checklist
19. Definition of Done

---

# 1. Purpose

Данный документ определяет единые стандарты разработки проекта SPAM.

Любой код, добавляемый в репозиторий, должен соответствовать этим требованиям.

---

# 2. Engineering Principles

Следуем принципам:

- Clean Architecture
- SOLID
- DRY
- KISS
- YAGNI
- Explicit is better than implicit
- Composition over inheritance
- Privacy by Design
- Security by Default

---

# 3. Project Structure

```
backend/

app/

bot/

core/

database/

middleware/

models/

repositories/

schemas/

services/

utils/

tests/
```

Каждая директория отвечает только за свою область ответственности.

Запрещается смешивать бизнес-логику и инфраструктурный код.

---

# 4. Python Style Guide

Используется:

- Python ≥ 3.14
- Ruff
- Black (совместимый стиль)
- mypy

Максимальная длина строки:

```
88 символов
```

Импорт:

```python
from pathlib import Path

from fastapi import APIRouter

from app.core.config import settings
```

Порядок:

1. stdlib
2. сторонние библиотеки
3. внутренние импорты

---

# 5. Naming Conventions

## Classes

```python
UserService
```

PascalCase.

---

## Functions

```python
create_user()
```

snake_case.

---

## Variables

```python
user_hash
database_url
```

snake_case.

---

## Constants

```python
MAX_MESSAGE_LENGTH
```

UPPER_CASE.

---

## Private Methods

```python
_generate_hash()
```

Начинаются с `_`.

---

# 6. Module Organization

Каждый модуль имеет следующую структуру:

```
feature/

handler.py

service.py

repository.py

schema.py

exceptions.py

utils.py
```

Правило зависимостей:

```
Handler

↓

Service

↓

Repository

↓

Database
```

Запрещено:

```
Handler

↓

Database
```

---

# 7. Database Standards

Используется SQLAlchemy ORM.

Raw SQL допускается только при документированной необходимости.

Каждая модель обязана иметь:

```python
id
created_at
updated_at
```

Если применимо — soft delete:

```python
deleted_at
```

Миграции выполняются только через Alembic.

Ручное изменение структуры БД запрещено.

---

# 8. API Standards

Все HTTP-маршруты:

```
/api/v1/
```

Ответы должны быть типизированы через Pydantic.

Ошибки должны возвращаться в едином формате:

```json
{
    "error": true,
    "message": "...",
    "code": "..."
}
```

---

# 9. Telegram Bot Standards

Каждая команда располагается в отдельном модуле.

Пример:

```
handlers/

start.py

profile.py

language.py

chat.py
```

Бизнес-логика внутри Handler запрещена.

Handler вызывает только Service.

---

# 10. Error Handling

Запрещается:

```python
except:
    pass
```

Используется:

```python
except Exception as exc:
    logger.exception(exc)
    raise
```

Каждое исключение должно иметь понятное сообщение.

---

# 11. Logging

Используется стандартный logging.

Логируются:

- ошибки;
- предупреждения;
- запуск сервисов;
- миграции;
- административные действия.

Не логируются:

- токены;
- пароли;
- приватные ключи;
- Telegram ID;
- IP-адреса (если они не требуются для защиты и не имеют отдельного обоснования).

---

# 12. Security

Обязательные требования:

- все секреты только через .env;
- параметризованные SQL-запросы;
- валидация входных данных;
- принцип минимальных привилегий.

Публичные идентификаторы пользователей не должны раскрывать внутренние идентификаторы системы.

---

# 13. Configuration

Все настройки находятся в:

```
app/core/config.py
```

Доступ:

```python
from app.core.config import settings
```

Запрещено:

```python
TOKEN = "123"
```

---

# 14. Testing

Каждый новый модуль сопровождается тестами.

Минимальный набор:

- unit;
- integration (при необходимости).

Перед коммитом выполняются:

```bash
ruff check .

pytest
```

---

# 15. Git Workflow

Каждый этап разработки:

```
Feature

↓

Test

↓

Commit

↓

Push
```

Формат сообщений:

```
feat:
fix:
refactor:
docs:
test:
chore:
ci:
```

Примеры:

```
feat: add anonymous identity

fix: resolve alembic configuration

docs: update architecture
```

---

# 16. Documentation

После каждого завершённого этапа обновляются:

- README.md
- CHANGELOG.md
- ROADMAP.md
- ARCHITECTURE.md
- DECISIONS.md

Если архитектурное решение изменилось — добавляется новый ADR.

---

# 17. Performance

Приоритеты:

1. Читаемость.
2. Надёжность.
3. Производительность.

Оптимизация проводится только после подтверждения узких мест измерениями.

---

# 18. Code Review Checklist

Перед объединением изменений убедиться, что:

- [ ] Код соответствует архитектуре.
- [ ] Нет дублирования.
- [ ] Пройдены тесты.
- [ ] Нет захардкоженных секретов.
- [ ] Добавлены миграции (если нужны).
- [ ] Обновлена документация.
- [ ] Добавлены типы.
- [ ] Добавлены комментарии там, где это действительно необходимо.

---

# 19. Definition of Done

Задача считается завершённой только если:

- Код реализован.
- Код проходит Ruff.
- Код проходит pytest.
- Миграции успешно применяются (если есть).
- Обновлена документация.
- Создан Git checkpoint.
- Изменения отправлены в GitHub.

---

# Основные принципы SPAM

1. Простые решения предпочтительнее сложных.
2. Архитектура важнее скорости написания.
3. Безопасность важнее удобства.
4. Документация — часть кода.
5. Один источник истины для конфигурации.
6. Один модуль — одна ответственность.
7. Любое изменение должно быть воспроизводимым.
8. Любое архитектурное решение должно быть задокументировано.
9. Любой новый разработчик должен понимать структуру проекта без устных объяснений.
10. Проект должен оставаться сопровождаемым через годы, а не только до первого релиза.

---

# Mission Statement

> **SPAM разрабатывается как долгосрочная инженерная платформа. Каждое техническое решение должно быть обоснованным, документированным, проверяемым и ориентированным на масштабируемость, безопасность и удобство сопровождения.**
