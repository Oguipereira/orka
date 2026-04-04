from sqlalchemy import Column, String, ForeignKey, Numeric, Text, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False, index=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False, index=True)
    predicted_demand = Column(Numeric(12, 2))
    prediction_date = Column(DateTime(timezone=True))
    confidence_score = Column(Numeric(5, 4))
    model_version = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Anomaly(Base):
    __tablename__ = "anomalies"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False, index=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), index=True)
    type = Column(String)  # queda, spike
    severity = Column(String)  # low, medium, high
    description = Column(Text)
    detected_at = Column(DateTime(timezone=True), server_default=func.now())
