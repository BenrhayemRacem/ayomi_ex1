from pydantic import BaseModel


class CreateExpressionDto(BaseModel):
    expression: str
