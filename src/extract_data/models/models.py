from dataclasses import dataclass

@dataclass
class WinamaxSport():
    sport_id: str
    sport_name: str

@dataclass
class WinamaxEvent():
    event_id: str
    event_name: str
    sport: WinamaxSport

@dataclass
class WinamaxEntity():
    entity_id: str
    entity_name: str

@dataclass
class WinamaxMatch():
    match_id: str
    match_name: str
    match_status: str
    event: WinamaxEvent
    entities: list[WinamaxEntity]
