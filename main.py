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
    """
    Return a single random inspirational quote.

    **Returns:**
    - **id**: Unique identifier for the quote (integer)
    - **text**: The quote text (string)
    - **author**: Author of the quote (string)
    - **category**: Category/tag for the quote (string)

    **Example response:**
    ```json
    {
      "id": 42,
      "text": "The only way to do great work is to love what you do.",
      "author": "Steve Jobs",
      "category": "motivation"
    }
    ```
    """
    if not quotes_db:
        raise HTTPException(status_code=404, detail="No quotes available")
    return random.choice(quotes_db)


@app.get("/quotes")
def get_all_quotes(category: Optional[str] = None) -> List[dict]:
    """
    Return all quotes, optionally filtered by category.

    **Parameters:**
    - **category** (optional): Filter quotes by category (e.g., "motivation", "life", "inspiration")

    **Returns:**
    - Array of quote objects, each containing:
      - **id**: Unique identifier (integer)
      - **text**: Quote text (string)
      - **author**: Author name (string)
      - **category**: Category/tag (string)

    **Example response (all quotes):**
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

    **Example response (filtered by category=motivation):**
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
    """
    if category:
        filtered = [q for q in quotes_db if q.get("category") == category]
        return filtered
    return quotes_db


@app.get("/quote/{quote_id}")
def get_quote_by_id(quote_id: int) -> dict:
    """
    Return a specific quote by its unique ID.

    **Parameters:**
    - **quote_id**: The unique numeric identifier of the quote

    **Returns:**
    - A single quote object with:
      - **id**: Unique identifier (integer)
      - **text**: Quote text (string)
      - **author**: Author name (string)
      - **category**: Category/tag (string)

    **Example response:**
    ```json
    {
      "id": 42,
      "text": "The only way to do great work is to love what you do.",
      "author": "Steve Jobs",
      "category": "motivation"
    }
    ```

    **Errors:**
    - **404**: Quote with the specified ID does not exist
    """
    for quote in quotes_db:
        if quote["id"] == quote_id:
            return quote
    raise HTTPException(status_code=404, detail=f"Quote with id {quote_id} not found")
