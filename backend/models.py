from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

# Association table for Site <-> Tag (many-to-many)
site_tags = Table(
    "site_tags",
    Base.metadata,
    Column("site_id", Integer, ForeignKey("sites.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)

    sites = relationship("Site", back_populates="category")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)

    sites = relationship("Site", secondary=site_tags, back_populates="tags")


class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    thumbnail = Column(String, nullable=True)         # auto-populated or optional
    description = Column(Text, nullable=True)
    favorite = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    category = relationship("Category", back_populates="sites")
    tags = relationship("Tag", secondary=site_tags, back_populates="sites")