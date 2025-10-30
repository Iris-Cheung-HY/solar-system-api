def test_get_all_planetsk_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_succeeds(client, one_saved_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Test Planet",
        "description": "nothing interesting",
        "mass": 2
    }



def test_create_one_planet(client):
    response = client.post("/planets", json={
        "name": "planet 111",
        "description": "description for test planet 111",
        "mass": 3
    })
    
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "planet 111",
        "description": "description for test planet 111",
        "mass": 3
    }