from fastapi import APIRouter
from retry import retry
from ..db.models.operation_model import OperationModel
from fastapi.responses import FileResponse
import csv

router = APIRouter()


@retry(delay=3, backoff=2, max_delay=12, tries=4)
@router.post("/operations", tags=["CSV"])
def export_operations():
    all_operations = OperationModel.select_all_operations()
    rows = [(op.id, op.expression, op.result) for op in all_operations]
    header = ["id", "expression", "result"]
    with open("operations.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)
    return {"detail": "CSV file created successfully", "header": header, "data": rows}


@retry(delay=3, backoff=2, max_delay=12, tries=4)
@router.get("/operations/download", tags=["CSV"])
def download_operations():
    all_operations = OperationModel.select_all_operations()
    rows = [(op.id, op.expression, op.result) for op in all_operations]
    header = ["id", "expression", "result"]
    with open("operations.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)
    return FileResponse(
        "operations.csv", filename="operations.csv", media_type="text/csv"
    )
