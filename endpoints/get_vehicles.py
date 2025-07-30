from fastapi import APIRouter,Depends
from sqlmodel import Session
from db.db import get_db
from models.vehicle_model import VehicleRead
from sqlmodel import Session
from typing import List
from db.vehicle_crud import get_vehicles


router=APIRouter()


@router.get(path="/get-vehicle", response_model = List[VehicleRead])
async def get_vehicle(numbers: int, db: Session=Depends(get_db)):
    vehicles= get_vehicles(db,numbers)
    return vehicles
