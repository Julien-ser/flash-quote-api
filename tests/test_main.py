import pytest
from fastapi.testclient import TestClient
from main import app, quotes_db

client = TestClient(app)


def test_get_random_quote():
    """Test that GET / returns a random quote with expected structure."""
    response = client.get("/")
    assert response.status_code == 200
    quote = response.json()
    assert "id" in quote
    assert "text" in quote
    assert "author" in quote
    assert "category" in quote
    assert isinstance(quote["id"], int)
    assert isinstance(quote["text"], str)
    assert isinstance(quote["author"], str)
    assert isinstance(quote["category"], str)


def test_get_all_quotes():
    """Test that GET /quotes returns all quotes."""
    response = client.get("/quotes")
    assert response.status_code == 200
    quotes = response.json()
    assert isinstance(quotes, list)
    assert len(quotes) > 0
    assert len(quotes) == len(quotes_db)


def test_get_quotes_by_category():
    """Test that GET /quotes with category filter returns only matching quotes."""
    # Get all unique categories
    categories = set(q["category"] for q in quotes_db)
    if categories:
        test_category = list(categories)[0]
        response = client.get(f"/quotes?category={test_category}")
        assert response.status_code == 200
        filtered = response.json()
        assert isinstance(filtered, list)
        for quote in filtered:
            assert quote["category"] == test_category


def test_get_quotes_invalid_category():
    """Test that GET /quotes with non-existent category returns empty list."""
    response = client.get("/quotes?category=nonexistent")
    assert response.status_code == 200
    quotes = response.json()
    assert quotes == []


def test_get_quote_by_id():
    """Test that GET /quote/{id} returns the correct quote."""
    if quotes_db:
        test_id = quotes_db[0]["id"]
        response = client.get(f"/quote/{test_id}")
        assert response.status_code == 200
        quote = response.json()
        assert quote["id"] == test_id


def test_get_quote_invalid_id():
    """Test that GET /quote/{id} with invalid ID returns 404."""
    response = client.get("/quote/999999")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data


def test_random_quote_diversity():
    """Test that multiple calls to random endpoint return varied quotes (no immediate repeats)."""
    if len(quotes_db) >= 2:
        responses = []
        for _ in range(10):
            response = client.get("/")
            responses.append(response.json()["id"])
        # Check that not all responses are the same (basic randomness check)
        assert len(set(responses)) > 1
