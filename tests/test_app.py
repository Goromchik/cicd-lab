from app import add, app


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data


def test_add_route():
    client = app.test_client()
    response = client.get("/add/4/6")
    assert response.status_code == 200
    assert response.get_json()["sum"] == 10
    