from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# table crawl_tasks 1.2
class CrawlTask(Base):
    __tablename__ = 'crawl_tasks'

    id = Column(Integer, primary_key=True)
    url_filter = Column(String, nullable=False)
    status = Column(String, default='Pending')  # Pending, In Progress, Done, Failed
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    businesses = relationship("BusinessData", back_populates="task")

# table business_data 1.2
class BusinessData(Base):
    __tablename__ = 'business_data'

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('crawl_tasks.id'))
    name = Column(String)
    phone = Column(String)
    address = Column(String)
    category = Column(String)
    website = Column(String)
    email = Column(String)

    task = relationship("CrawlTask", back_populates="businesses")
