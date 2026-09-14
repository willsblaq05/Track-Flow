from datetime import datetime, timezone
from sqlmodel import Field, SQLModel

class Hub(SQLModel, table=True):
    __tablename__ = 'hubs'

    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    city: str = Field(nullable=False)
    state: str = Field(nullable=False)
    latitude: float = Field(nullable=True)
    longitude: float = Field(nullable=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": datetime.now(timezone.utc)})