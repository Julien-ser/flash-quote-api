# flash-quote-api
**Mission:** A tiny FastAPI service that returns random inspirational quotes.

## Phase 1: Planning & Setup
- [x] Define the quote data structure (e.g., JSON array with fields: id, text, author, category)
- [x] Choose storage method: in-memory array vs JSON file vs SQLite database
- [x] Initialize FastAPI project with uv (Python 3.9+) or pip + virtualenv
- [x] Set up basic project structure: main.py, quotes_data.json, tests/, requirements.txt

## Phase 2: Core Development
- [x] Create quotes_data.json with at least 50 inspirational quotes
- [x] Implement GET / endpoint that returns a single random quote
- [x] Implement GET /quotes endpoint that returns all quotes (with optional ?category= filter)
- [x] Implement optional GET /quote/{id} endpoint for specific quote retrieval

## Phase 3: Testing & Quality
- [x] Write unit tests for quote selection algorithm (ensure randomness, no repeats in succession)
- [x] Write integration tests for all endpoints using httpx or requests
- [x] Add custom exception handling for invalid quote IDs and missing categories
- [x] Configure CORS middleware for cross-origin requests (public API)

## Phase 4: Documentation & Deployment
- [x] Generate OpenAPI/Swagger docs with FastAPI automatic docs
- [x] Write README.md with API endpoint documentation and example responses
 - [x] Create Dockerfile for containerized deployment
 - [x] Set up GitHub Actions for CI: linting (ruff), testing on push
```
