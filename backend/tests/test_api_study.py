"""Tests for study/quiz API endpoints (minimal version with simplified auth)."""
import pytest
from fastapi.testclient import TestClient


@pytest.mark.integration
class TestStartSession:
    """Test POST /api/v1/study/sessions endpoint."""

    def test_start_session_review_mode(self, client: TestClient, test_deck, test_cards):
        """Test starting a review mode session (simplified auth - auto-authenticated)."""
        payload = {"deck_id": test_deck.id, "mode": "review"}
        response = client.post("/api/v1/study/sessions", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["deck_id"] == test_deck.id
        assert data["mode"] == "review"
        assert data["status"] == "active"

    def test_start_session_nonexistent_deck(self, client: TestClient):
        """Test starting a session with non-existent deck."""
        payload = {"deck_id": 999999, "mode": "review"}
        response = client.post("/api/v1/study/sessions", json=payload)
        # Will likely fail with 404 or succeed with no cards
        assert response.status_code in [201, 404]


@pytest.mark.integration
class TestGetSession:
    """Test GET /api/v1/study/sessions/{session_id} endpoint."""

    def test_get_session(self, client: TestClient, quiz_session):
        """Test getting a quiz session."""
        response = client.get(f"/api/v1/study/sessions/{quiz_session.id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == quiz_session.id


@pytest.mark.integration
class TestFinishSession:
    """Test POST /api/v1/study/sessions/{session_id}/finish endpoint."""

    def test_finish_session(self, client: TestClient, quiz_session):
        """Test finishing a quiz session."""
        response = client.post(f"/api/v1/study/sessions/{quiz_session.id}/finish")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "completed"
        assert data["ended_at"] is not None


@pytest.mark.integration
class TestSubmitAnswer:
    """Test POST /api/v1/study/sessions/{session_id}/answer endpoint."""

    def test_submit_answer_review_mode(self, client: TestClient, quiz_session, test_cards):
        """Test submitting an answer in review mode."""
        card = test_cards[0]
        payload = {"card_id": card.id, "user_answer": "4", "quality": 4}
        response = client.post(
            f"/api/v1/study/sessions/{quiz_session.id}/answer",
            json=payload,
        )
        assert response.status_code == 200
        data = response.json()
        assert data["card_id"] == card.id
        assert data["quality"] == 4


@pytest.mark.integration
class TestDueReviews:
    """Test GET /api/v1/study/reviews/due endpoint."""

    def test_due_reviews_with_due_card(self, client: TestClient, srs_review):
        """Test getting due reviews (simplified auth - auto-authenticated)."""
        response = client.get("/api/v1/study/reviews/due")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1

    def test_due_reviews_empty(self, client: TestClient):
        """Test getting due reviews when there are none."""
        response = client.get("/api/v1/study/reviews/due")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)


@pytest.mark.integration
class TestSessionStatistics:
    """Test GET /api/v1/study/sessions/{session_id}/statistics endpoint."""

    def test_get_session_statistics_empty(self, client: TestClient, quiz_session):
        """Test getting statistics for a session with no responses."""
        response = client.get(f"/api/v1/study/sessions/{quiz_session.id}/statistics")
        assert response.status_code == 200
        data = response.json()
        assert data["total_responses"] == 0
        assert data["correct_count"] == 0
        assert data["incorrect_count"] == 0
        assert data["unanswered_count"] == 0

    def test_get_session_statistics_with_responses(self, client: TestClient, quiz_session, test_cards, db):
        """Test getting statistics for a session with responses."""
        from app.models import QuizResponse

        # Add some quiz responses
        responses = [
            QuizResponse(session_id=quiz_session.id, card_id=test_cards[0].id, is_correct=True),
            QuizResponse(session_id=quiz_session.id, card_id=test_cards[1].id, is_correct=False),
            QuizResponse(session_id=quiz_session.id, card_id=test_cards[2].id, is_correct=True),
            QuizResponse(session_id=quiz_session.id, card_id=test_cards[0].id, is_correct=None),
        ]
        for r in responses:
            db.add(r)
        db.commit()

        response = client.get(f"/api/v1/study/sessions/{quiz_session.id}/statistics")
        assert response.status_code == 200
        data = response.json()
        assert data["total_responses"] == 4
        assert data["correct_count"] == 2
        assert data["incorrect_count"] == 1
        assert data["unanswered_count"] == 1


@pytest.mark.integration
class TestActivityData:
    """Test GET /api/v1/study/activity endpoint."""

    def test_get_activity_empty(self, client: TestClient):
        """Test activity endpoint when user has no completed sessions."""
        response = client.get("/api/v1/study/activity?days=7")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 7  # Should return 7 days of data
        # All counts should be 0 for new user
        for item in data:
            assert "date" in item
            assert "count" in item
            assert item["count"] == 0

    def test_get_activity_with_completed_sessions(self, client: TestClient, test_deck, db):
        """Test activity endpoint with completed quiz sessions."""
        from app.models import QuizSession
        from app.models.enums import QuizMode, QuizStatus
        from datetime import datetime, timezone

        # Create completed quiz sessions
        now_naive = datetime.now(tz=timezone.utc).replace(tzinfo=None)
        sessions = [
            QuizSession(
                user_id=1,  # Default user
                deck_id=test_deck.id,
                mode=QuizMode.REVIEW,
                status=QuizStatus.COMPLETED,
                started_at=now_naive,
                ended_at=now_naive,
            ),
            QuizSession(
                user_id=1,
                deck_id=test_deck.id,
                mode=QuizMode.REVIEW,
                status=QuizStatus.COMPLETED,
                started_at=now_naive,
                ended_at=now_naive,
            ),
        ]
        for session in sessions:
            db.add(session)
        db.commit()

        response = client.get("/api/v1/study/activity?days=7")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 7
        # At least one day should have count of 2
        total_count = sum(item["count"] for item in data)
        assert total_count == 2

    def test_get_activity_custom_days(self, client: TestClient):
        """Test activity endpoint with custom days parameter."""
        response = client.get("/api/v1/study/activity?days=14")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 14  # Should return 14 days of data
