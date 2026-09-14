from datetime import datetime, timezone
from sqlmodel import Field, SQLModel

class ShipmentEvent(SQLModel, table=True):
    __tablename__ = 'shipment_events'

    id: int = Field(default=None, primary_key=True)
    shipment_id: int = Field(foreign_key="shipments.id", nullable=False)
    status: str = Field(nullable=False)
    description: str = Field(nullable=True)
    hub_id: int = Field(foreign_key="hubs.id", nullable=True)   
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))