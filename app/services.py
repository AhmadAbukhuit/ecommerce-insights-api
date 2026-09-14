import pandas as pd


def load_data(filepath: str):
    df = pd.read_csv(filepath)
    df['Total_Sales'] = df['Quantity'] * df['Unit_Price']
    return df

def get_summary_metrics(df):
    total_revenue = float(df['Total_Sales'].sum())
    total_orders = len(df)
    average_order = total_revenue / total_orders
    
    return {
        "total_revenue": round(total_revenue, 2),
        "total_orders": total_orders,
        "average_order_value": round(average_order, 2)
    }

def get_category_revenue(df):
    summary = df.groupby('Category')['Total_Sales'].sum().to_dict()
    return {k: round(v, 2) for k, v in summary.items()}