import json

def test_create_user(client):
    response = client.post("/users", json={"name": "Teste", "email": "teste@example.com"})
    assert response.status_code == 201
    assert response.get_json()["name"] == "Teste"

def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_user(client):
    # Primeiro cria
    post = client.post("/users", json={"name": "Fulano", "email": "fulano@example.com"})
    user_id = post.get_json()["id"]
    # Depois busca
    get = client.get(f"/users/{user_id}")
    assert get.status_code == 200
    assert get.get_json()["name"] == "Fulano"

def test_update_user(client):
    post = client.post("/users", json={"name": "Antes", "email": "antes@example.com"})
    user_id = post.get_json()["id"]
    put = client.put(f"/users/{user_id}", json={"name": "Depois"})
    assert put.status_code == 200
    assert put.get_json()["name"] == "Depois"

def test_delete_user(client):
    post = client.post("/users", json={"name": "Excluir", "email": "excluir@example.com"})
    user_id = post.get_json()["id"]
    delete = client.delete(f"/users/{user_id}")
    assert delete.status_code == 204
