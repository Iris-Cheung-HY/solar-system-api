def test_get_all_moons_with_no_records(client):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_moons(client, one_saved_moon):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Moon1",
        "mass":5,
        "description":"bright",
        "planet": None,
        "planet_id": None,
    }]

def test_create_one_moon(client):
    # Act
    response = client.post("/moons", json={
        "name": "Moon1",
        "description": "bright",
        "mass":5
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Moon1",
        "description": "bright",
        "mass":5,
        "planet": None,
        "planet_id": None,
    }