from pydantic import BaseModel, Field


class SummaryMetricsResponse(BaseModel):
    """Summary KPI metrics calculated across all sales transactions."""

    total_revenue: float = Field(
        ...,
        description="Total gross sales revenue across all transactions",
        examples=[124500.75],
    )
    total_orders: int = Field(
        ...,
        description="Total number of processed transaction records",
        examples=[500],
    )
    average_order_value: float = Field(
        ...,
        description="Average revenue per transaction order",
        examples=[249.0],
    )


class HealthResponse(BaseModel):
    """Health status and data readiness response."""

    status: str = Field(default="healthy", description="Current service health status")
    total_records: int = Field(
        ..., description="Total transaction records loaded into memory"
    )
    version: str = Field(default="1.0.0", description="API semantic version")


class MessageResponse(BaseModel):
    """Generic informational response."""

    message: str = Field(..., description="Descriptive status or welcome message")


class TransactionBase(BaseModel):
    """Base schema for an e-commerce transaction."""

    Category: str = Field(
        ...,
        description="Product department / category",
        examples=["Electronics"],
    )
    Unit_Price: float = Field(
        ...,
        gt=0,
        description="Price per single item in USD, must be greater than 0",
        examples=[99.99],
    )
    Quantity: int = Field(
        ...,
        ge=1,
        description="Item quantity purchased, must be at least 1",
        examples=[2],
    )


class TransactionCreate(TransactionBase):
    """Schema for adding a new transaction."""



class TransactionResponse(TransactionBase):
    """Schema for a transaction with generated fields."""

    Transaction_ID: str = Field(..., description="Unique transaction identifier")
    Date: str = Field(..., description="Transaction date (YYYY-MM-DD)")
    Total_Sales: float = Field(..., description="Calculated total line item revenue")
