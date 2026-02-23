from fastapi import APIRouter
from store import satellitestore

router = APIRouter(prefix="/satellites", tags=["satellites"])

@router.get("/")
def list_satellites():
    return satellitestore.rows