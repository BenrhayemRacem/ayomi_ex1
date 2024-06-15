from sqlalchemy import Column, Integer, Text, TIMESTAMP, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker, scoped_session
from ..db import DB
from typing import List

Base = declarative_base()
DBSession = scoped_session(sessionmaker(bind=DB().engine))


class StepModel(Base):
    __tablename__ = "step"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
    index = Column(Integer)
    execution = Column(Text)
    operation_id = Column(Integer, nullable=False)
    updated_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )

    def __init__(self, index, execution, operation_id):
        self.index = index
        self.execution = execution
        self.operation_id = operation_id

    @staticmethod
    def get_steps_by_operation_id(operation_id):
        session = DBSession()
        try:
            steps_select = select(StepModel).where(
                StepModel.operation_id == operation_id
            )
            return session.scalars(steps_select).all()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def select_all():
        session = DBSession()
        try:
            steps_select = select(StepModel)
            return session.scalars(steps_select).all()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def insert_many(new_steps: List["StepModel"]):
        session = DBSession()
        try:
            session.add_all(new_steps)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
