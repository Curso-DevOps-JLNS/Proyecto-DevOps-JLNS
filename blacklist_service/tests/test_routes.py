import pytest
from unittest.mock import patch, MagicMock
from app.models import BlacklistEntry
from app.schemas import BlacklistSchema
from app.routes import STATIC_TOKEN
from faker import Faker
from run import create_app


fake = Faker()

@pytest.fixture
def client():
    class TestConfig:
        TESTING = True
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        JWT_SECRET_KEY = "test-secret"

    app = create_app(TestConfig)

    with app.app_context():
        from app.models import db
        db.create_all()

    with app.test_client() as client:
        yield client

def auth_header():
    return {"Authorization": f"Bearer {STATIC_TOKEN}"}

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

@patch("app.routes.db.session")
@patch("app.routes.BlacklistEntry")
def test_post_blacklist_valid(mock_blacklist_entry, mock_session, client):
    payload = {
        "email": fake.email(),
        "app_uuid": fake.uuid4(),
        "blocked_reason": fake.sentence(nb_words=3)
    }
    mock_instance = MagicMock()
    mock_blacklist_entry.return_value = mock_instance

    response = client.post("/blacklists", json=payload, headers=auth_header())

    assert response.status_code == 201
    assert response.get_json() == {"message": "Email added to blacklist"}
    assert mock_session.add.called
    assert mock_session.commit.called

@patch("app.routes.db.session")
def test_post_blacklist_invalid_payload(mock_session, client):
    payload = {
        "app_uuid": fake.uuid4()
    }
    response = client.post("/blacklists", json=payload, headers=auth_header())
    assert response.status_code == 400
    assert "errors" in response.get_json()

def test_check_blacklisted_email(client):
    from app.models import db, BlacklistEntry

    email = fake.email()
    reason = fake.sentence(nb_words=2)
    ip_address = fake.ipv4()

    with client.application.app_context():
        entry = BlacklistEntry(
            email=email,
            app_uuid=fake.uuid4(),
            blocked_reason=reason,
            ip_address=ip_address
        )
        db.session.add(entry)
        db.session.commit()

    response = client.get(f"/blacklists/{email}", headers=auth_header())
    assert response.status_code == 200
    assert response.get_json() == {"blacklisted": True, "reason": reason}

def test_check_non_blacklisted_email(client):
    email = fake.email()

    response = client.get(f"/blacklists/{email}", headers=auth_header())
    assert response.status_code == 200
    assert response.get_json() == {"blacklisted": False}

