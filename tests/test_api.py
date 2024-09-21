import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from src.api.auth.dependencies import JWTBearer
from src.api.auth.utils import sign_jwt
from src.api.app import create_app

app = create_app()
testclient = TestClient(app)

def test_unauth_route():
    response = testclient.get("/notes/")
    assert response.status_code == 403

# def test_signup():
#     data = {
#         "fullname": "Kozhemyaka Artem Alexsandrovich",
#         "email": "tvoyo_mblLo@mail.ru",
#         "password": "password",
#     }
#     response = testclient.post("/users/signup", json=data)
#     assert response.status_code == 200

def test_login():
    data= {
        "email": "tvoyo_mblLo@mail.ru",
        "password": "password",
    }
    response = testclient.post("/users/login", json=data)
    assert response.status_code == 200

def test_post_note():
    data = {
        "text": "string"
    }
    testclient.headers["Authorization"] = "Bearer token"
    with patch.object(JWTBearer, "verify_jwt", return_value=True):
        
            response = testclient.post("/notes/", json=data)
            assert response.status_code == 403
            assert response.text == ""

