from fastapi import APIRouter
from endpoints.add_vehicles import router as add_vehicle
from endpoints.get_vehicles import router as get_vehicle

router=APIRouter(prefix="/V1",tags=["Vehicles"])
router.include_router(add_vehicle)
router.include_router(get_vehicle)