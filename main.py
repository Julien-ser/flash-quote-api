import json
import random
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="flash-quote-api", version="1.0.0")

# Enable CORS for public API access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load quotes from JSON file into memory at startup
def load_quotes() -> List[dict]:
    try:
        with open("quotes_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


quotes_db = load_quotes()


@app.get("/")
def get_random_quote() -> dict:
    """Return a single random quote."""
    if not quotes_db:
        raise HTTPException(status_code=404, detail="No quotes available")
    return random.choice(quotes_db)


@app.get("/quotes")
def get_all_quotes(category: Optional[str] = None) -> List[dict]:
    """Return all quotes, optionally filtered by category."""
    if category:
        filtered = [q for q in quotes_db if q.get("category") == category]
        return filtered
    return quotes_db


@app.get("/quote/{quote_id}")
def get_quote_by_id(quote_id: int) -> dict:
    """Return a specific quote by ID."""
    for quote in quotes_db:
        if quote["id"] == quote_id:
            return quote
    raise HTTPException(status_code=404, detail=f"Quote with id {quote_id} not found")
