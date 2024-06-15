from sqlalchemy import Column, Integer, Text, TIMESTAMP, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker, scoped_session
from ..db import DB

Base = declarative_base()
DBSession = scoped_session(sessionmaker(bind=DB().engine))


class OperationModel(Base):
    __tablename__ = "operation"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
    expression = Column(Text)
    result = Column(Text)
    updated_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )

    @staticmethod
    def get_one_by_id(id):
        session = DBSession()
        try:
            result_select = select(OperationModel).where(OperationModel.id == id)
            return session.scalars(result_select).one()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def select_all_operations():
        session = DBSession()
        try:
            operations_select = select(OperationModel)
            return session.scalars(operations_select).all()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def insert_one(expression, result):
        session = DBSession()
        try:
            new_operation = OperationModel(
                expression=expression,
                result=result,
            )
            session.add(new_operation)
            session.commit()
            session.refresh(new_operation)
            return new_operation
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
