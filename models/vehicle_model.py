from sqlmodel import SQLModel, Field
from typing import Optional


class VehicleBase(SQLModel):
    name: str
    color: str
    brand: str
    rent: int

class VehicleCreate(VehicleBase):   # Used for request body (input)
    pass

class VehicleRead(VehicleBase):   # Used for response
    id:int

class Vehicle(VehicleBase,table=True):   # table_model
    id: Optional[int] = Field(default=None, primary_key=True)
