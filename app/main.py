import os

from fastapi import FastAPI, HTTPException
from services import get_category_revenue, get_summary_metrics, load_data

# Ensure data exists; if not, instruct user to generate it
if not os.path.exists('sales_data.csv'):
    raise FileNotFoundError("sales_data.csv not found. Run generate_data.py first.")

df = load_data('sales_data.csv')

app = FastAPI(
    title="Real-Time Insights API",
    description="A demonstration API for dynamic e-commerce data analysis.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-Commerce API. Navigate to /docs to test."}

@app.get("/metrics/summary")
def summary():
    return get_summary_metrics(df)

@app.get("/metrics/category")
def category_breakdown(category_name: str | None = None):
    data = get_category_revenue(df)
    
    if category_name:
        if category_name not in data:
            raise HTTPException(status_code=404, detail="Category not found")
        return {category_name: data[category_name]}
    
    return data