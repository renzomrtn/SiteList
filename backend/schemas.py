from datetime import datetime
from typing import Optional
from pydantic import BaseModel, HttpUrl


# ── Tag ──────────────────────────────────────────────────────────────────────

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagRead(TagBase):
    id: int

    model_config = {"from_attributes": True}


# ── Category ──────────────────────────────────────────────────────────────────

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: int

    model_config = {"from_attributes": True}


# ── Site ──────────────────────────────────────────────────────────────────────

class SiteCreate(BaseModel):
    name: str
    url: str                        # e.g. "dribbble.com"
    description: Optional[str] = None
    thumbnail: Optional[str] = None # manually supplied or left blank
    favorite: bool = False
    category: Optional[str] = None  # category name — created if it doesn't exist
    tags: list[str] = []            # tag names — created if they don't exist

class SiteUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    description: Optional[str] = None
    thumbnail: Optional[str] = None
    favorite: Optional[bool] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None

class SiteRead(BaseModel):
    id: int
    name: str
    url: str
    thumbnail: Optional[str]
    description: Optional[str]
    favorite: bool
    created_at: datetime
    category: Optional[CategoryRead]
    tags: list[TagRead]

    model_config = {"from_attributes": True}