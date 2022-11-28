from fastapi import Body, Depends, FastAPI
from fastapi.security import HTTPBasic
from db_models import Session, StatModel
from queries import retrieve_all_instances, delete_all_instances, create_instance
from typing import List
from pydantic_models import RetrieveStat, CreateStat, RetrieveQueryParams

app = FastAPI()
auth = HTTPBasic()


def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.post("/retrieve_items", response_model=List[RetrieveStat])
def retreive_stat_instance(item: RetrieveQueryParams, db: Session = Depends(get_session)):
    return retrieve_all_instances(db, StatModel, item)

@app.post("/create_item", response_model=List[RetrieveStat])
def create_stat_instance(item: CreateStat, db: Session = Depends(get_session)):
    return create_instance(db, StatModel, item)

@app.post("/delete")
def statistics_view(db: Session = Depends(get_session)):
    delete_all_instances(db, StatModel)
    return 'All Stat items have been deleted'
