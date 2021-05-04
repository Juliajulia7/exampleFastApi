from fastapi import APIRouter
from typing import List, Optional
from ..models.operations import Operation, CheckBox, OperationCreate, OperationUpdate
from fastapi import Depends, Response, status
from ..services.operations import OperationService

router = APIRouter(
    prefix = '/operations',
)


@router.get('/', response_model=List[Operation])
def get_operations(result: Optional[CheckBox] = None,
                   service: OperationService = Depends()):
    return service.get_list(result=result)

@router.post('/', response_model=Operation)
def create_operation(
        operation_data: OperationCreate,
        service: OperationService = Depends(),
):
    return service.create(operation_data)

@router.get('/{operation_uid}', response_model=Operation)
def operation(
        operation_uid: int,
        service: OperationService = Depends(),
):
    return service.get(operation_uid)

@router.put('/{operation_uid}', response_model=Operation)
def update_operation(
        operation_uid: int,
        operation_data: OperationUpdate,
        service: OperationService = Depends(),
):
    return service.update(operation_uid, operation_data)

@router.get('/{operation_uid}')
def delete_operation(
        operation_uid: int,
        service: OperationService = Depends(),
):
    service.delete(operation_uid)
    return Response(status_code = status.HTTP_204_NO_CONTENT)
