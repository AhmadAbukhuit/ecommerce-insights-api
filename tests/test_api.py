from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.json()
    assert "message" in json_data
    assert "Welcome" in json_data["message"]


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["total_records"] > 0
    assert data["version"] == "1.0.0"


def test_metrics_summary():
    response = client.get("/metrics/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_revenue" in data
    assert "total_orders" in data
    assert "average_order_value" in data
    assert data["total_orders"] > 0
    assert data["total_revenue"] > 0


def test_category_breakdown_all():
    response = client.get("/metrics/category")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0


def test_category_breakdown_single():
    # Fetch all categories first to get a valid category name
    all_categories = client.get("/metrics/category").json()
    assert len(all_categories) > 0
    valid_category = next(iter(all_categories.keys()))

    response = client.get(f"/metrics/category?category_name={valid_category}")
    assert response.status_code == 200
    data = response.json()
    assert valid_category in data
    assert isinstance(data[valid_category], (int, float))


def test_category_breakdown_not_found():
    response = client.get("/metrics/category?category_name=NonExistentCategoryXYZ")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Category not found"
