from db_models import Session, DeclarativeBase
from pydantic_models import RetrieveQueryParams, RetrieveStat


def create_instance(session: Session, model: DeclarativeBase, item: RetrieveStat) -> DeclarativeBase:
    instance = model(**item.dict())
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return [instance]

def retrieve_all_instances(session: Session, model: DeclarativeBase, item: RetrieveQueryParams) -> DeclarativeBase:
    query = session.query(model).filter(model.date.between(item.start, item.end)).order_by(model.date.desc()).all()
    return query

def delete_all_instances(session: Session, model: DeclarativeBase) -> DeclarativeBase:
    session.query(model).delete()
    session.commit()
