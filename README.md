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
- ✅ Storage method: JSON file loaded into memory at startup
- ⬜ Initialize FastAPI project with uv/pip
- ⬜ Set up tests directory and add unit tests

See [TASKS.md](TASKS.md) for full development roadmap.
