# flash-quote-api

A tiny FastAPI service that returns random inspirational quotes.

## Architecture

**Storage Design:**
- Quotes are stored in `quotes_data.json` (JSON array with id, text, author, category)
- On startup, the entire JSON file is loaded into memory as a Python list
- All API endpoints read from this in-memory array for maximum performance
- This approach provides O(1) random access and O(n) category filtering with minimal overhead

**Trade-offs:**
- ✅ Fast read performance (no database queries)
- ✅ Simple implementation and maintenance
- ✅ No external dependencies beyond FastAPI
- ⚠️ Data is read-only at runtime (modify JSON file to update quotes)
- ⚠️ Memory usage scales with quote count (negligible for <1000 quotes)

## Quick Start

### Local Development

```bash
# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload
```

### Docker Deployment

```bash
# Build the Docker image
docker build -t flash-quote-api .

# Run the container
docker run -p 8000:8000 flash-quote-api
```

The API will be available at http://localhost:8000

## API Documentation

The API provides three endpoints for accessing inspirational quotes. FastAPI automatically generates interactive OpenAPI/Swagger documentation at:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

#### GET / (Root)

Returns a single random quote.

**Response:**
```json
{
  "id": 42,
  "text": "The only way to do great work is to love what you do.",
  "author": "Steve Jobs",
  "category": "motivation"
}
```

#### GET /quotes

Returns all quotes, with optional category filtering.

**Query Parameters:**
- `category` (optional): Filter quotes by category (e.g., "motivation", "life", "inspiration")

**Example (all quotes):**
```json
[
  {
    "id": 1,
    "text": "The only way to do great work is to love what you do.",
    "author": "Steve Jobs",
    "category": "motivation"
  },
  {
    "id": 2,
    "text": "Life is what happens when you're busy making other plans.",
    "author": "John Lennon",
    "category": "life"
  }
]
```

**Example (filtered by category=motivation):**
```json
[
  {
    "id": 1,
    "text": "The only way to do great work is to love what you do.",
    "author": "Steve Jobs",
    "category": "motivation"
  }
]
```

#### GET /quote/{quote_id}

Returns a specific quote by its unique ID.

**Path Parameters:**
- `quote_id`: The unique numeric identifier of the quote

**Example response:**
```json
{
  "id": 42,
  "text": "The only way to do great work is to love what you do.",
  "author": "Steve Jobs",
  "category": "motivation"
}
```

**Error responses:**
- `404 Not Found`: When the specified quote ID does not exist

## Project Status

**Phase 1: Planning & Setup**
- ✅ Quote data structure defined (JSON with id, text, author, category)
- ✅ Storage method: JSON file loaded into memory at startup
- ✅ Initialize FastAPI project with uv/pip
- ✅ Set up tests directory and add unit tests

See [TASKS.md](TASKS.md) for full development roadmap.
