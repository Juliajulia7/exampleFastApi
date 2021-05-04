from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum

class CheckBox(str, Enum):
    DONE = 'done'
    NOTDONE = 'notdone'

class OperationBase(BaseModel):
    date: date
    uid: int
    title: str
    description: Optional[str]
    result: CheckBox

class Operation(OperationBase):
  id : int

  class Config:
      orm_mode=True

class OperationCreate(OperationBase):
    pass

class OperationUpdate(OperationBase):
    pass