"""Tests for deck API endpoints (minimal version with simplified auth)."""
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models import Card, Deck, User


@pytest.mark.integration
class TestListDecks:
    """Test GET /api/v1/decks endpoint."""

    def test_list_decks(self, client: TestClient, test_deck):
        """Test listing decks (simplified auth - auto-authenticated)."""
        response = client.get("/api/v1/decks")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1

    def test_list_decks_with_search(self, client: TestClient, test_deck):
        """Test listing decks with search query."""
        response = client.get("/api/v1/decks?q=Test")
        assert response.status_code == 200
        data = response.json()
        assert any(deck["title"] == "Test Deck" for deck in data)

    def test_list_decks_with_limit(self, client: TestClient, test_deck):
        """Test listing decks with limit parameter."""
        response = client.get("/api/v1/decks?limit=1")
        assert response.status_code == 200
        data = response.json()
        assert len(data) <= 1


@pytest.mark.integration
class TestReadDeck:
    """Test GET /api/v1/decks/{deck_id} endpoint."""

    def test_read_deck(self, client: TestClient, test_deck):
        """Test reading a deck."""
        response = client.get(f"/api/v1/decks/{test_deck.id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == test_deck.id
        assert data["title"] == test_deck.title

    def test_read_nonexistent_deck(self, client: TestClient):
        """Test reading a non-existent deck returns 404."""
        response = client.get("/api/v1/decks/999999")
        assert response.status_code == 404


@pytest.mark.integration
class TestCreateDeck:
    """Test POST /api/v1/decks endpoint."""

    def test_create_deck(self, client: TestClient):
        """Test creating a deck (simplified auth - auto-authenticated)."""
        payload = {
            "title": "New Deck",
            "description": "A new test deck",
            "is_public": True,
            "cards": [],
        }
        response = client.post("/api/v1/decks", json=payload)
        # In simplified auth, all requests are authenticated
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "New Deck"
        assert data["is_public"] is True

    def test_create_deck_with_basic_cards(self, client: TestClient):
        """Test creating a deck with basic cards."""
        payload = {
            "title": "Deck with Cards",
            "description": "Test",
            "is_public": True,
            "cards": [
                {
                    "type": "basic",
                    "prompt": "What is 1+1?",
                    "answer": "2",
                }
            ],
        }
        response = client.post("/api/v1/decks", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert len(data["cards"]) == 1
        assert data["cards"][0]["type"] == "basic"

    def test_create_deck_validation_error(self, client: TestClient):
        """Test creating a deck with missing required fields."""
        payload = {"description": "Missing title"}
        response = client.post("/api/v1/decks", json=payload)
        assert response.status_code == 422


@pytest.mark.integration
class TestUpdateDeck:
    """Test PUT /api/v1/decks/{deck_id} endpoint."""

    def test_update_deck(self, client: TestClient, test_deck):
        """Test updating a deck."""
        payload = {"title": "Updated Title", "description": "Updated description"}
        response = client.put(f"/api/v1/decks/{test_deck.id}", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"


@pytest.mark.integration
class TestDeleteDeck:
    """Test DELETE /api/v1/decks/{deck_id} endpoint."""

    def test_delete_deck(self, client: TestClient, db: Session, test_user: User):
        """Test deleting a deck."""
        # Create a deck to delete
        deck = Deck(
            title="To Delete",
            description="Will be deleted",
            is_public=True,
            owner_user_id=test_user.id,
        )
        db.add(deck)
        db.commit()
        db.refresh(deck)

        response = client.delete(f"/api/v1/decks/{deck.id}")
        assert response.status_code == 200

    def test_delete_nonexistent_deck(self, client: TestClient):
        """Test deleting a non-existent deck returns 404."""
        response = client.delete("/api/v1/decks/99999")
        assert response.status_code == 404

    def test_delete_deck_with_cards_cascade(self, client: TestClient, db: Session, test_user: User):
        """Test deleting a deck cascades to delete its cards."""
        # Create a deck with cards
        deck = Deck(
            title="Deck with Cards",
            description="Has cards",
            is_public=True,
            owner_user_id=test_user.id,
        )
        db.add(deck)
        db.commit()
        db.refresh(deck)

        # Add some cards
        card1 = Card(deck_id=deck.id, type="basic", prompt="Q1", answer="A1")
        card2 = Card(deck_id=deck.id, type="basic", prompt="Q2", answer="A2")
        db.add(card1)
        db.add(card2)
        db.commit()

        # Delete the deck
        response = client.delete(f"/api/v1/decks/{deck.id}")
        assert response.status_code == 200

        # Verify deck is deleted
        deleted_deck = db.get(Deck, deck.id)
        assert deleted_deck is None

        # Verify cards are also deleted (cascade)
        deleted_card1 = db.get(Card, card1.id)
        deleted_card2 = db.get(Card, card2.id)
        assert deleted_card1 is None
        assert deleted_card2 is None


@pytest.mark.integration
class TestAddCard:
    """Test POST /api/v1/decks/{deck_id}/cards endpoint."""

    def test_add_basic_card(self, client: TestClient, test_deck):
        """Test adding a basic card to a deck."""
        payload = {
            "type": "basic",
            "prompt": "New card question?",
            "answer": "New card answer",
        }
        response = client.post(f"/api/v1/decks/{test_deck.id}/cards", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["prompt"] == "New card question?"
        assert data["type"] == "basic"


@pytest.mark.integration
class TestEditCard:
    """Test PUT /api/v1/decks/cards/{card_id} endpoint."""

    def test_edit_card(self, client: TestClient, test_cards):
        """Test editing a card."""
        card = test_cards[0]
        payload = {"prompt": "Updated question?", "answer": "Updated answer"}
        response = client.put(f"/api/v1/decks/cards/{card.id}", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["prompt"] == "Updated question?"


@pytest.mark.integration
class TestRemoveCard:
    """Test DELETE /api/v1/decks/cards/{card_id} endpoint."""

    def test_remove_card(self, client: TestClient, test_cards):
        """Test removing a card."""
        card = test_cards[0]
        response = client.delete(f"/api/v1/decks/cards/{card.id}")
        assert response.status_code == 200

    def test_remove_nonexistent_card(self, client: TestClient):
        """Test removing a non-existent card returns 404."""
        response = client.delete("/api/v1/decks/cards/999999")
        assert response.status_code == 404
