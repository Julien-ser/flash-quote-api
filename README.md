# flash-quote-api

A tiny FastAPI service that returns random inspirational quotes.

## Overview

This is a simple REST API that provides:
- Random inspirational quotes
- Quote collection browsing
- Category filtering
- OpenAPI/Swagger documentation

## Quick Start

```bash
# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload
```

Visit http://localhost:8000/docs for interactive API documentation.

## Project Status

**Phase 1: Planning & Setup**
- ✅ Quote data structure defined (JSON with id, text, author, category)
- ⬜ Choose storage method
- ⬜ Initialize FastAPI project
- ⬜ Set up basic project structure

See [TASKS.md](TASKS.md) for full development roadmap.
