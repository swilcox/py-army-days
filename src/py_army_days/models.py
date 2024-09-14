from datetime import datetime

from pydantic import BaseModel, Field


class ConfigModel(BaseModel):
    use_army_butt_days: bool = Field(default=False, alias="useArmyButtDays")
    show_completed: bool = Field(default=False, alias="showCompleted")


class EntryModel(BaseModel):
    title: str
    date: datetime


class DaysModel(BaseModel):
    config: ConfigModel
    entries: list[EntryModel]


class ComputedEventModel(EntryModel):
    days: float
