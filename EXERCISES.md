# 🎓 Student Exercises & Hands-on Labs

Welcome to the hands-on lab section for the **Real-Time E-Commerce Insights Engine**! These exercises are designed to guide you step-by-step through modern backend API development with **FastAPI**, data analysis with **Pandas**, automated testing with **pytest**, and containerization with **Docker**.

---

## Table of Contents

- [Lab 1: Add a Health Check Endpoint (Beginner)](#lab-1-add-a-health-check-endpoint-beginner)
- [Lab 2: Implement Date Range Filtering with Pandas (Intermediate)](#lab-2-implement-date-range-filtering-with-pandas-intermediate)
- [Lab 3: Build a Top Categories Endpoint (Intermediate)](#lab-3-build-a-top-categories-endpoint-intermediate)
- [Lab 4: Create a Transaction Ingestion Endpoint - HTTP POST (Advanced)](#lab-4-create-a-transaction-ingestion-endpoint---http-post-advanced)
- [Lab 5: Test-Driven Development (TDD) with Pytest (Quality Assurance)](#lab-5-test-driven-development-tdd-with-pytest-quality-assurance)

---

## Lab 1: Add a Health Check Endpoint (Beginner)

### 🎯 Objective

Expose a `GET /health` endpoint that returns the API's operational status and the count of loaded records.

### 📚 Concepts Taught

- Defining response schemas using Pydantic `BaseModel`.
- Registering GET route handlers in FastAPI.
- Viewing auto-generated Swagger documentation at `/docs`.

### 🛠️ Tasks

1. In `app/schemas.py`, review the `HealthResponse` model:

   ```python
   class HealthResponse(BaseModel):
       status: str
       total_records: int
       version: str
   ```

2. In `app/main.py`, ensure the route is registered:

   ```python
   @app.get("/health", response_model=HealthResponse)
   def health_check():
       return {
           "status": "healthy",
           "total_records": len(df),
           "version": app.version,
       }
   ```

3. Test your work:

   ```bash
   curl http://localhost:8000/health
   # Expected output: {"status":"healthy","total_records":500,"version":"1.0.0"}
   ```

---

## Lab 2: Implement Date Range Filtering with Pandas (Intermediate)

### 🎯 Objective

Allow clients to filter summary metrics by a date range using query parameters:
`GET /metrics/summary?start_date=2026-08-01&end_date=2026-08-31`

### 📚 Concepts Taught

- Optional query parameters in FastAPI (`Query`).
- Filtering Pandas DataFrames with boolean masks.
- Validating ISO dates (`YYYY-MM-DD`).

### 🛠️ Tasks

1. In `app/services.py`, update `get_summary_metrics` to accept optional `start_date` and `end_date`:

   ```python
   def get_summary_metrics(df, start_date: str | None = None, end_date: str | None = None):
       filtered_df = df
       if start_date:
           filtered_df = filtered_df[filtered_df['Date'] >= start_date]
       if end_date:
           filtered_df = filtered_df[filtered_df['Date'] <= end_date]

       if filtered_df.empty:
           return {"total_revenue": 0.0, "total_orders": 0, "average_order_value": 0.0}

       total_revenue = float(filtered_df['Total_Sales'].sum())
       total_orders = len(filtered_df)
       average_order = total_revenue / total_orders

       return {
           "total_revenue": round(total_revenue, 2),
           "total_orders": total_orders,
           "average_order_value": round(average_order, 2)
       }
   ```

2. In `app/main.py`, pass `start_date` and `end_date` from the route parameters to `get_summary_metrics(df, start_date, end_date)`.
3. Verify in your browser at `http://localhost:8000/docs`.

---

## Lab 3: Build a Top Categories Endpoint (Intermediate)

### 🎯 Objective

Create a `GET /metrics/top-categories?limit=3` endpoint that returns categories ranked by highest sales revenue.

### 📚 Concepts Taught

- Pandas `.sort_values(ascending=False)` and `.head(n)`.
- Query parameter constraints (e.g., `Query(default=3, ge=1, le=10)`).
- Returning structured lists of objects in responses.

### 🛠️ Tasks

1. In `app/schemas.py`, create a `TopCategoryItem` schema:

   ```python
   class TopCategoryItem(BaseModel):
       category: str
       total_revenue: float
   ```

2. In `app/services.py`, write a function `get_top_categories(df, limit: int = 3)`:

   ```python
   def get_top_categories(df, limit: int = 3):
       grouped = df.groupby('Category')['Total_Sales'].sum().reset_index()
       sorted_df = grouped.sort_values(by='Total_Sales', ascending=False).head(limit)
       return [
           {"category": row['Category'], "total_revenue": round(row['Total_Sales'], 2)}
           for _, row in sorted_df.iterrows()
       ]
   ```

3. Expose the route in `app/main.py`:

   ```python
   @app.get("/metrics/top-categories", response_model=list[TopCategoryItem])
   def top_categories(limit: int = 3):
       return get_top_categories(df, limit=limit)
   ```

---

## Lab 4: Create a Transaction Ingestion Endpoint - HTTP POST (Advanced)

### 🎯 Objective

Implement `POST /transactions` to accept a new sale, validate its fields, compute its line total, and append it to the dataset.

### 📚 Concepts Taught

- HTTP POST and request body validation.
- Setting HTTP status codes (`status_code=201`).
- Appending rows to a Pandas DataFrame or CSV file.

### 🛠️ Tasks

1. In `app/schemas.py`, verify `TransactionCreate` has input constraints:

   ```python
   class TransactionCreate(BaseModel):
       Category: str
       Unit_Price: float = Field(..., gt=0)
       Quantity: int = Field(..., ge=1)
   ```

2. In `app/main.py`, implement the endpoint:

   ```python
   from datetime import datetime, timezone
   from schemas import TransactionCreate, TransactionResponse

   @app.post("/transactions", response_model=TransactionResponse, status_code=201)
   def create_transaction(item: TransactionCreate):
       global df
       new_id = f"TXN-{1000 + len(df) + 1}"
       today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
       total = round(item.Unit_Price * item.Quantity, 2)

       new_row = pd.DataFrame([{
           "Transaction_ID": new_id,
           "Date": today,
           "Category": item.Category,
           "Unit_Price": item.Unit_Price,
           "Quantity": item.Quantity,
           "Total_Sales": total
       }])
       df = pd.concat([df, new_row], ignore_index=True)

       return {
           "Transaction_ID": new_id,
           "Date": today,
           "Category": item.Category,
           "Unit_Price": item.Unit_Price,
           "Quantity": item.Quantity,
           "Total_Sales": total
       }
   ```

3. Test using `curl`:

   ```bash
   curl -X POST http://localhost:8000/transactions \
     -H "Content-Type: application/json" \
     -d '{"Category": "Electronics", "Unit_Price": 199.99, "Quantity": 2}'
   ```

4. Query `/metrics/summary` again to confirm that total orders and revenue updated immediately!

---

## Lab 5: Test-Driven Development (TDD) with Pytest (Quality Assurance)

### 🎯 Objective

Write comprehensive tests for your new endpoints and calculation functions before writing the production code.

### 📚 Concepts Taught

- Using `pytest` and `fastapi.testclient.TestClient`.
- Testing edge cases (negative values, empty inputs, non-existent records).
- Asserting HTTP status codes (200, 201, 404, 422).

### 🛠️ Tasks

1. Add a test in `tests/test_api.py` that asserts that submitting a negative `Unit_Price` returns HTTP 422 (Unprocessable Entity):

   ```python
   def test_create_transaction_invalid_price():
       payload = {"Category": "Toys", "Unit_Price": -10.0, "Quantity": 1}
       response = client.post("/transactions", json=payload)
       assert response.status_code == 422
   ```

2. Run your test suite with:

   ```bash
   make test
   # or: pytest -v
   ```

---

## 🌟 Bonus Challenge: Docker & CI/CD

1. Add a `HEALTHCHECK` command to the `Dockerfile`:

   ```dockerfile
   HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
     CMD curl -f http://localhost:8000/health || exit 1
   ```

2. Trigger the GitHub Actions CI workflows by opening a pull request with your solutions!
