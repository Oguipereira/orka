from sqlalchemy import Column, String, ForeignKey, Numeric, Text, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base

class Decision(Base):
    __tablename__ = "decisions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False, index=True)
    type = Column(String)       # reabastecimento, price_adjust, promocao, alerta
    priority = Column(String)   # baixa, media, alta
    title = Column(String)
    description = Column(Text)
    recommended_action = Column(Text)
    confidence_score = Column(Numeric(5, 4))
    status = Column(String, default="pendente")  # pendente, aprovado, executado, ignorado
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DecisionLog(Base):
    __tablename__ = "decision_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    decision_id = Column(UUID(as_uuid=True), ForeignKey("decisions.id"), nullable=False, index=True)
    action_taken = Column(Text)
    result = Column(Text)
    executed_at = Column(DateTime(timezone=True), server_default=func.now())
