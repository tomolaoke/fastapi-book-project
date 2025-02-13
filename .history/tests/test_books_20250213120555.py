from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_book():
    # Test valid book
    response = client.get("/api/v1/books/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    
    # Test invalid book
    response = client.get("/api/v1/books/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book Not Found"}

def test_get_all_books():
    response = client.get("/api/v1/books/")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_single_book():
    response = client.get("/api/v1/books/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"

def test_create_book():
    new_book = {
        "id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": "Fantasy",
    }
    response = client.post("/api/v1/books/", json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 4
    assert data["title"] == "Harry Potter and the Sorcerer's Stone"

def test_update_book():
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put("/api/v1/books/1", json=updated_book)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit: An Unexpected Journey"

def test_delete_book():
    response = client.delete("/api/v1/books/3")
    assert response.status_code == 204

    response = client.get("/api/v1/books/3")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book Not Found"}
