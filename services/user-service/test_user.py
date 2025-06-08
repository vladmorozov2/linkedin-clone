from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


class TestFastAPIApp:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)


def test_app_no_error():
    response = client.get("/")
    assert response.status_code < 500


class TestUser:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)

    def test_create_user(self):
        payload = {"username": "vlad123", "password": "asd123asd"}
        response = client.post(
            "user/", json={"username": "vlad123", "password": "asd123asd"}
        )
        assert response.status_code == 200
