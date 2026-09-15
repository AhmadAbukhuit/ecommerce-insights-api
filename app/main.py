import sys
from pathlib import Path

# Ensure app directory is in Python path for flexible import resolution
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from fastapi import FastAPI, HTTPException
from schemas import (
    HealthResponse,
    MessageResponse,
    SummaryMetricsResponse,
)
from services import get_category_revenue, get_summary_metrics, load_data

DATA_FILE = BASE_DIR / "sales_data.csv"

# Ensure data exists; if not, instruct user to generate it
if not DATA_FILE.exists():
    raise FileNotFoundError(f"{DATA_FILE.name} not found. Run generate_data.py first.")

df = load_data(str(DATA_FILE))

app = FastAPI(
    title="Real-Time Insights API",
    description="A demonstration API for dynamic e-commerce data analysis.",
    version="1.0.0",
)


@app.get("/", response_model=MessageResponse)
def read_root():
    return {"message": "Welcome to the E-Commerce API. Navigate to /docs to test."}


@app.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "healthy",
        "total_records": len(df),
        "version": app.version,
    }


@app.get("/metrics/summary", response_model=SummaryMetricsResponse)
def summary():
    return get_summary_metrics(df)


@app.get("/metrics/category", response_model=dict[str, float])
def category_breakdown(category_name: str | None = None):
    data = get_category_revenue(df)

    if category_name:
        if category_name not in data:
            raise HTTPException(status_code=404, detail="Category not found")
        return {category_name: data[category_name]}

    return data