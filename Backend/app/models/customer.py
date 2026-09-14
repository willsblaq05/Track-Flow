from datetime import datetime, timezone
from sqlmodel import Field, SQLModel

class Customer(SQLModel, table=True):
    __tablename__ = 'customers'

    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    email: str = Field(index=True, nullable=False, unique=True)
    phone_number: str = Field(nullable=True)
    address: str = Field(nullable=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": datetime.now(timezone.utc)})