from fastapi import APIRouter, Depends
from models.vehicle_model import VehicleCreate,VehicleRead
from sqlmodel import Session
from db.db import get_db
from db.vehicle_crud import insert_vehicles
from typing import List


router = APIRouter()

@router.post(path="/add_vehicles",response_model=List[VehicleRead])
async def add_vehicles(vehicles : List[VehicleCreate], db: Session=Depends(get_db)):
            return insert_vehicles(db, vehicles)


