from datetime import datetime, timezone
from sqlmodel import Field, SQLModel

class Shipment(SQLModel, table=True):
    __tablename__ = 'shipments'

    id: int = Field(default=None, primary_key=True)
    tracking_number: str = Field(index=True, nullable=False, unique=True)
    customer_id: int = Field(foreign_key="customers.id", nullable=False)
    origin_hub_id: int = Field(foreign_key="hubs.id", nullable=False)
    status: str = Field(default='created', nullable=False)
    destination_hub_id: int = Field(foreign_key="hubs.id", nullable=True)
    current_hub_id: int = Field(foreign_key="hubs.id", nullable=True)
    expected_delivery_date: datetime = Field(nullable=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": datetime.now(timezone.utc)})