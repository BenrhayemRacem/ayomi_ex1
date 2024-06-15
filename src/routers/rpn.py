from fastapi import APIRouter, HTTPException
from retry import retry
from ..services.rpn_service import RpnService
from ..db.models.operation_model import OperationModel
from ..db.models.step_model import StepModel
from ..dto.create_expression_dto import CreateExpressionDto
from sqlalchemy.exc import NoResultFound

router = APIRouter()


@retry(delay=3, backoff=2, max_delay=12, tries=4)
@router.post("/", tags=["RPN"])
def evaluate(create_expression_dto: CreateExpressionDto):
    try:
        rpn_service = RpnService()
        expression = create_expression_dto.expression
        rpn_service.validate(expression=expression)
        result, steps = rpn_service.evaluate(expression=expression)
        inserted_operation = OperationModel.insert_one(
            expression=expression, result=result
        )
        inserted_opeation_id = inserted_operation.id
        steps_records = []
        for idx, step_execution in enumerate(steps):
            steps_records.append(
                StepModel(
                    index=idx,
                    execution=step_execution,
                    operation_id=inserted_opeation_id,
                )
            )
        StepModel.insert_many(new_steps=steps_records)
        return {"success": True, "data": result}
    except ValueError as value_error:
        raise HTTPException(status_code=400, detail=str(value_error))
    except ZeroDivisionError as zero_division_error:
        raise HTTPException(status_code=400, detail=str(zero_division_error))


@retry(delay=3, backoff=2, max_delay=12, tries=4)
@router.get("/operations", tags=["RPN"])
def get_operations():
    all_operations = OperationModel.select_all_operations()
    return all_operations


@retry(delay=3, backoff=2, max_delay=12, tries=4)
@router.get("/operations/{id}", tags=["RPN"])
def get_operations(id):
    try:
        operation = OperationModel.get_one_by_id(id=id)
        return operation
    except NoResultFound:
        raise HTTPException(404, f"no operation found with id: {id}")


@retry(delay=3, backoff=2, max_delay=12, tries=4)
@router.get("/steps/operation/{operation_id}", tags=["RPN"])
def get_operations(operation_id):
    try:
        steps = StepModel.get_steps_by_operation_id(operation_id=operation_id)
        return steps
    except NoResultFound:
        raise HTTPException(404, f"no steps found with operation_id: {operation_id}")
