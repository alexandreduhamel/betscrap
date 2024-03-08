from pydantic import BaseModel


class WinamaxSport(BaseModel):
    sport_id: str
    sport_name: str


class WinamaxEvent(BaseModel):
    event_id: str
    event_name: str
    category_id: str
    category_name: str
    tournament_id: str
    tournament_name: str
    sport: WinamaxSport


class WinamaxMatch(BaseModel):
    match_id: str
    match_name: str
    match_status: str
    sport_id: str
    category_id: str
    tournament_id: str


class WinamaxEntity(BaseModel):
    entity_id: str
    entity_name: str
