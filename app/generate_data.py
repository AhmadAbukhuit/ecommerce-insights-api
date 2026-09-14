import csv
import random
from datetime import datetime, timedelta, timezone

categories = ['Electronics', 'Clothing', 'Home', 'Toys']

with open('sales_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Transaction_ID', 'Date', 'Category', 'Unit_Price', 'Quantity'])
    for i in range(1, 501):
        writer.writerow([
            f"TXN-{1000+i}",
            (datetime.now(timezone.utc) - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'),
            random.choice(categories),
            round(random.uniform(10.0, 500.0), 2),
            random.randint(1, 5)
        ])
print("sales_data.csv generated successfully.")