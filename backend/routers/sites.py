from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from models import Site, Category, Tag
from schemas import SiteCreate, SiteRead, SiteUpdate

router = APIRouter(prefix="/sites", tags=["Sites"])


# ── Helpers ───────────────────────────────────────────────────────────────────

def _get_or_create_category(db: Session, name: str) -> Category:
    category = db.query(Category).filter(Category.name == name).first()
    if not category:
        category = Category(name=name)
        db.add(category)
        db.flush()
    return category


def _get_or_create_tags(db: Session, names: list[str]) -> list[Tag]:
    tags = []
    for name in names:
        tag = db.query(Tag).filter(Tag.name == name).first()
        if not tag:
            tag = Tag(name=name)
            db.add(tag)
            db.flush()
        tags.append(tag)
    return tags


# ── Routes ────────────────────────────────────────────────────────────────────

@router.get("/", response_model=list[SiteRead])
def list_sites(
    favorite: bool | None = Query(default=None),
    category: str | None = Query(default=None),
    tag: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    """List all sites. Optionally filter by favorite, category name, or tag name."""
    q = db.query(Site)
    if favorite is not None:
        q = q.filter(Site.favorite == favorite)
    if category:
        q = q.join(Site.category).filter(Category.name == category)
    if tag:
        q = q.join(Site.tags).filter(Tag.name == tag)
    return q.all()


@router.post("/", response_model=SiteRead, status_code=201)
def create_site(payload: SiteCreate, db: Session = Depends(get_db)):
    """Create a new site. Category and tags are created automatically if they don't exist."""
    if db.query(Site).filter(Site.url == payload.url).first():
        raise HTTPException(status_code=409, detail="A site with that URL already exists.")

    category = _get_or_create_category(db, payload.category) if payload.category else None
    tags = _get_or_create_tags(db, payload.tags)

    site = Site(
        name=payload.name,
        url=payload.url,
        description=payload.description,
        thumbnail=payload.thumbnail,
        favorite=payload.favorite,
        category=category,
        tags=tags,
    )
    db.add(site)
    db.commit()
    db.refresh(site)
    return site


@router.get("/{site_id}", response_model=SiteRead)
def get_site(site_id: int, db: Session = Depends(get_db)):
    site = db.query(Site).filter(Site.id == site_id).first()
    if not site:
        raise HTTPException(status_code=404, detail="Site not found.")
    return site


@router.patch("/{site_id}", response_model=SiteRead)
def update_site(site_id: int, payload: SiteUpdate, db: Session = Depends(get_db)):
    site = db.query(Site).filter(Site.id == site_id).first()
    if not site:
        raise HTTPException(status_code=404, detail="Site not found.")

    if payload.name is not None:
        site.name = payload.name
    if payload.url is not None:
        site.url = payload.url
    if payload.description is not None:
        site.description = payload.description
    if payload.thumbnail is not None:
        site.thumbnail = payload.thumbnail
    if payload.favorite is not None:
        site.favorite = payload.favorite
    if payload.category is not None:
        site.category = _get_or_create_category(db, payload.category)
    if payload.tags is not None:
        site.tags = _get_or_create_tags(db, payload.tags)

    db.commit()
    db.refresh(site)
    return site


@router.delete("/{site_id}", status_code=204)
def delete_site(site_id: int, db: Session = Depends(get_db)):
    site = db.query(Site).filter(Site.id == site_id).first()
    if not site:
        raise HTTPException(status_code=404, detail="Site not found.")
    db.delete(site)
    db.commit()