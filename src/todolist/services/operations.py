from typing import List, Optional

from fastapi import Depends, HTTPException, status

from .. import tables
from ..datebase import get_session
from todolist.datebase import Session
from ..models.operations import CheckBox, OperationCreate, OperationUpdate


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    def get(self, operaton_uid: int) -> tables.Operation:
        operaton = [
            self.session
            .query(tables.Operation)
            .filter_by(uid=operaton_uid)
            .first()
        ]
        if not operaton:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operaton

    def get_list(self, result: Optional[CheckBox] = None)->List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if result:
            query = query.filter_by(result=result)
        operations = query.all()
        return operations

    def get(self, operaton_uid: int) -> tables.Operation:
        return self.get(operaton_uid)

    def create(self, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, operation_uid: int, operator_data: OperationUpdate)->tables.Operation:
        operation = self._get(operation_uid)
        for field, value in operator_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, operation_uid: int):
        operation = self._get(operation_uid)
        self.session.delete(operation)
        self.session.commit()