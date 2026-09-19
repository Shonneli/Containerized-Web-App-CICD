import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def client():
    # Redis isn't running during CI tests, so we mock it out
    with patch("redis.Redis") as mock_redis:
        mock_instance = MagicMock()
        mock_instance.incr.return_value = 1
        mock_redis.return_value = mock_instance

        import app
        app.app.config["TESTING"] = True
        with app.app.test_client() as test_client:
            yield test_client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_contains_expected_text(client):
    response = client.get("/")
    assert b"Docker Compose Demo" in response.data