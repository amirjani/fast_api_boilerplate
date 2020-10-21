from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator

from app.schemas.core import CoreModel, DateTimeModelMixin, IDModelMixin


class CountryBase(CoreModel):
    name: Optional[str] = None
    code: Optional[str] = None
    calling_code: Optional[int] = None,
    region: Optional[str] = None,
    translation: Optional[dict] = None,
    flag: Optional[str] = None
    created_at: Optional[datetime]
    deleted_at: Optional[datetime]


class CountryCreate(CountryBase):
    name: str
    code: str
    calling_code: int
    region: str
    translation: list
    flag: str
    created_at = datetime.now()


class CountryUpdate(CountryBase):
    pass


class CountryInDBBase(CountryBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Country(CountryInDBBase):
    pass