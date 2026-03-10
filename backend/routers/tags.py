from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Tag
from schemas import TagCreate, TagRead

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.get("/", response_model=list[TagRead])
def list_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()


@router.post("/", response_model=TagRead, status_code=201)
def create_tag(payload: TagCreate, db: Session = Depends(get_db)):
    if db.query(Tag).filter(Tag.name == payload.name).first():
        raise HTTPException(status_code=409, detail="Tag already exists.")
    tag = Tag(name=payload.name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


@router.delete("/{tag_id}", status_code=204)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found.")
    db.delete(tag)
    db.commit()