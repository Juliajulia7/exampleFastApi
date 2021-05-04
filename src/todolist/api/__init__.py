from fastapi import APIRouter
from .operations import router as oro

router = APIRouter()
router.include_router(oro)