import io

import pandas as pd

from app.services import get_category_revenue, get_summary_metrics, load_data


def test_load_data():
    csv_content = """Transaction_ID,Date,Category,Unit_Price,Quantity
TXN-1,2026-01-01,Electronics,100.0,2
TXN-2,2026-01-02,Clothing,50.0,3
"""
    df = load_data(io.StringIO(csv_content))

    assert "Total_Sales" in df.columns
    assert len(df) == 2
    assert df.loc[0, "Total_Sales"] == 200.0
    assert df.loc[1, "Total_Sales"] == 150.0


def test_get_summary_metrics():
    df = pd.DataFrame({
        "Transaction_ID": ["TXN-1", "TXN-2", "TXN-3"],
        "Category": ["Electronics", "Clothing", "Electronics"],
        "Unit_Price": [100.0, 50.0, 25.0],
        "Quantity": [2, 1, 4],
        "Total_Sales": [200.0, 50.0, 100.0],
    })

    metrics = get_summary_metrics(df)

    assert metrics["total_revenue"] == 350.0
    assert metrics["total_orders"] == 3
    assert metrics["average_order_value"] == round(350.0 / 3, 2)


def test_get_category_revenue():
    df = pd.DataFrame({
        "Transaction_ID": ["TXN-1", "TXN-2", "TXN-3"],
        "Category": ["Electronics", "Clothing", "Electronics"],
        "Total_Sales": [200.0, 50.0, 100.0],
    })

    revenue = get_category_revenue(df)

    assert revenue["Electronics"] == 300.0
    assert revenue["Clothing"] == 50.0
