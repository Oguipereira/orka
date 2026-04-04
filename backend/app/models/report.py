from sqlalchemy import Column, String, ForeignKey, Text, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base

class Report(Base):
    __tablename__ = "reports"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False, index=True)
    type = Column(String)   # mensal, semanal
    summary = Column(Text)
    generated_at = Column(DateTime(timezone=True), server_default=func.now())

class ReportItem(Base):
    __tablename__ = "report_items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    report_id = Column(UUID(as_uuid=True), ForeignKey("reports.id"), nullable=False, index=True)
    section = Column(String)  # resumo, problemas, oportunidades, plano
    content = Column(Text)
