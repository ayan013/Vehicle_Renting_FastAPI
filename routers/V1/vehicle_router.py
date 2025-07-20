from fastapi import APIRouter
from endpoints.vehicles import router as vehicles_router

router=APIRouter(prefix="/V1",tags=["Vehicles"])
router.include_router(vehicles_router)