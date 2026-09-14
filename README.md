# Real-Time E-Commerce Insights Engine 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)

A comprehensive Python demonstration project showcasing the integration of data analysis (**Pandas**) with modern backend web delivery (**FastAPI**).

## Features

* **Dynamic Data Ingestion:** Automates the parsing of raw e-commerce transaction data.
* **On-the-fly Analytics:** Calculates key performance indicators (KPIs) including total revenue, average order value, and categorical breakdowns.
* **RESTful Delivery:** Exposes business logic through a fast, automatically documented API.
* **Containerized Environment:** Fully supported Docker deployment for seamless execution across all platforms.

## Quick Start (Local Setup)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AhmadAbukhuit/ecommerce-insights-api.git
   cd ecommerce-insights-api
   ```

2. **Create a virtual environment and install dependencies:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Generate the sample dataset:**

    ```bash
    python generate_data.py
    ```

4. **Run the development server:**

    ```bash
    uvicorn main:app --reload
    ```

5. **Test the API:**

    Open [http://127.0.0.0:8000/docs](http://127.0.0.0:8000/docs) in your browser.

## Quick Start (Docker)

If you have Docker installed, you can launch the entire stack with one command:

```bash
docker-compose up --build
```

The API and Swagger UI will be available at [http://127.0.0.0:8000/docs](http://127.0.0.0:8000/docs).
