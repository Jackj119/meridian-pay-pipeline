from app import create_app


def test_create_app_returns_flask_instance():
    app = create_app()
    assert app is not None
    assert app.name == "app"


def test_health_status_code_and_body(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_health_content_type_is_json(client):
    response = client.get("/health")
    assert response.content_type == "application/json"


def test_health_rejects_post(client):
    response = client.post("/health")
    assert response.status_code == 405


def test_index_status_code_and_body(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to Meridian Pay Pipeline"}


def test_index_content_type_is_json(client):
    response = client.get("/")
    assert response.content_type == "application/json"


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404
