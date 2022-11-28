from datetime import date
from pydantic import BaseModel, root_validator
import typing


class RetrieveStat(BaseModel):
    id: int
    date: date
    views: int
    clicks: int
    cost: float
    cpc: typing.Optional[float]
    cpm: typing.Optional[float]

    @root_validator
    def compute_fields(cls, values) -> typing.Dict:
        if values["clicks"] == 0:
            values["cpc"] = 0
        else:
            values["cpc"] = values["cost"] * values["clicks"]

        if values["views"] == 0:
            values["cpm"] = 0
        else:
            values["cpm"] = values["cost"] / values["views"] * 1000

        return values

    class Config:
        orm_mode = True

class RetrieveQueryParams(BaseModel):
    start: date
    end: date

class CreateStat(BaseModel):
    date: date
    views: int
    clicks: int
    cost: float

    class Config:
        orm_mode = True