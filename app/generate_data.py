import csv
import secrets
from datetime import datetime, timedelta, timezone
from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parent / "sales_data.csv"
categories = ["Electronics", "Clothing", "Home", "Toys"]

rng = secrets.SystemRandom()

with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Transaction_ID", "Date", "Category", "Unit_Price", "Quantity"])
    for i in range(1, 501):
        writer.writerow([
            f"TXN-{1000 + i}",
            (datetime.now(timezone.utc) - timedelta(days=rng.randint(0, 30))).strftime(
                "%Y-%m-%d"
            ),
            rng.choice(categories),
            round(rng.uniform(10.0, 500.0), 2),
            rng.randint(1, 5),
        ])

print(f"{OUTPUT_PATH.name} generated successfully at {OUTPUT_PATH}.")