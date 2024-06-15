from fastapi import FastAPI
from src.routers import rpn, csv

app = FastAPI()

app.include_router(router=rpn.router, prefix="/rpn")

app.include_router(router=csv.router, prefix="/csv")
