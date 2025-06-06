from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app import models

client = TestClient(app)

def setup_module():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        test_user = models.User(name="testuser")
        db.add(test_user)
        db.commit()
    finally:
        db.close()

def teardown_module():
    models.Base.metadata.drop_all(bind=engine)

def test_create_user():
    response = client.post("/users/", json={"name": "newuser"})
    assert response.status_code == 201
    assert response.json()["name"] == "newuser"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_user_posts():
    response = client.get("/users/1/posts")
    assert response.status_code in [200, 404]

def test_create_post():
    response = client.post("/posts/", json={"text": "Test post", "user_id": 1})
    assert response.status_code == 201
    assert response.json()["text"] == "Test post"