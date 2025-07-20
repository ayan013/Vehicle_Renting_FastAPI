from sqlmodel import Session
from models.vehicle_model import Vehicle, VehicleCreate
from typing import List

def insert_vehicles(db: Session, vehicles: List[VehicleCreate]) -> List[Vehicle]:
    vehicle_all=[Vehicle(**v.model_dump()) for v in vehicles]
    db.add_all(vehicle_all)
    db.commit()
    for v in vehicle_all:
        db.refresh(v)
    return vehicle_all