from pydantic import BaseModel


class WinamaxSport(BaseModel):
    sport_id: str
    sport_name: str


class WinamaxEvent(BaseModel):
    event_id: str
    event_name: str
    sport: WinamaxSport


class WinamaxEntity(BaseModel):
    entity_id: str
    entity_name: str


class WinamaxMatch(BaseModel):
    match_id: str
    match_name: str
    match_status: str
    event: WinamaxEvent
    entities: list[WinamaxEntity]
