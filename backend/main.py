from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers import sites, categories, tags

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Site Dictionary API",
    description="A curated dictionary of useful websites, organized by category and tags.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sites.router)
app.include_router(categories.router)
app.include_router(tags.router)


@app.get("/", tags=["Health"])
def root():
    return {"message": "Site Dictionary API is running."}