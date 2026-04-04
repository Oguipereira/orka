from sqlalchemy import Column, ForeignKey, Numeric, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base

class Metric(Base):
    __tablename__ = "metrics"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False, index=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    revenue = Column(Numeric(12, 2))
    cost = Column(Numeric(12, 2))
    margin = Column(Numeric(8, 4))
    growth_rate = Column(Numeric(8, 4))
    stock_turnover = Column(Numeric(8, 4))
    trend_score = Column(Numeric(8, 4))
