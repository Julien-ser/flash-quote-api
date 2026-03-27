# flash-quote-api
**Mission:** A tiny FastAPI service that returns random inspirational quotes.

## Phase 1: Planning & Setup
- [ ] Define the quote data structure (e.g., JSON array with fields: id, text, author, category)
- [ ] Choose storage method: in-memory array vs JSON file vs SQLite database
- [ ] Initialize FastAPI project with uv (Python 3.9+) or pip + virtualenv
- [ ] Set up basic project structure: main.py, quotes_data.json, tests/, requirements.txt

## Phase 2: Core Development
- [ ] Create quotes_data.json with at least 50 inspirational quotes
- [ ] Implement GET / endpoint that returns a single random quote
- [ ] Implement GET /quotes endpoint that returns all quotes (with optional ?category= filter)
- [ ] Implement optional GET /quote/{id} endpoint for specific quote retrieval

## Phase 3: Testing & Quality
- [ ] Write unit tests for quote selection algorithm (ensure randomness, no repeats in succession)
- [ ] Write integration tests for all endpoints using httpx or requests
- [ ] Add custom exception handling for invalid quote IDs and missing categories
- [ ] Configure CORS middleware for cross-origin requests (public API)

## Phase 4: Documentation & Deployment
- [ ] Generate OpenAPI/Swagger docs with FastAPI automatic docs
- [ ] Write README.md with API endpoint documentation and example responses
- [ ] Create Dockerfile for containerized deployment
- [ ] Set up GitHub Actions for CI: linting (ruff), testing on push
```
