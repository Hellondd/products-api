def make(client, name="Ноутбук", price=1000, in_stock=True):
    return client.post(
        "/products",
        json={"name": name, "price": price, "in_stock": in_stock},
    )


def test_create_product(client):
    r = make(client)
    assert r.status_code == 201
    body = r.json()
    assert body["id"] == 1
    assert body["name"] == "Ноутбук"
    assert body["in_stock"] is True


def test_in_stock_default_true(client):
    r = client.post("/products", json={"name": "Мышь", "price": 10})
    assert r.status_code == 201
    assert r.json()["in_stock"] is True


def test_duplicate_name_conflict(client):
    make(client)
    assert make(client).status_code == 409


def test_invalid_data(client):
    assert make(client, name="A").status_code == 422
    assert make(client, name="x" * 81).status_code == 422
    assert make(client, price=-1).status_code == 422


def test_get_product(client):
    pid = make(client).json()["id"]
    assert client.get(f"/products/{pid}").status_code == 200
    assert client.get("/products/999").status_code == 404


def test_put_replaces_product(client):
    pid = make(client).json()["id"]
    r = client.put(
        f"/products/{pid}",
        json={"name": "Телефон", "price": 500, "in_stock": False},
    )
    assert r.status_code == 200
    assert r.json()["name"] == "Телефон"
    assert r.json()["in_stock"] is False


def test_put_duplicate_name(client):
    make(client, name="Товар А")
    pid = make(client, name="Товар Б").json()["id"]
    r = client.put(
        f"/products/{pid}",
        json={"name": "Товар А", "price": 1, "in_stock": True},
    )
    assert r.status_code == 409


def test_put_not_found(client):
    r = client.put(
        "/products/999",
        json={"name": "Телефон", "price": 1, "in_stock": True},
    )
    assert r.status_code == 404


def test_delete_product(client):
    pid = make(client).json()["id"]
    assert client.delete(f"/products/{pid}").status_code == 204
    assert client.get(f"/products/{pid}").status_code == 404
    assert client.delete(f"/products/{pid}").status_code == 404