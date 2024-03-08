import json
import urllib
import urllib.error
import urllib.request
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from models import WinamaxSport, WinamaxMatch, WinamaxEntity, WinamaxEvent


URL_HOME = "https://www.winamax.fr/paris-sportifs"
URL_MATCH = "https://www.winamax.fr/paris-sportifs/match/"
URL_SPORT = "https://www.winamax.fr/paris-sportifs/sports/"
URL_BOOST = "https://www.winamax.fr/paris-sportifs/sports/100000"


def parse_from_url(url) -> dict:
    """
    This function sends a request to the specified winamax URL and
    returns a dictionary containing key-value pairs extracted from the HTML

    Args:
        url (str): The URL of the page to request.

    Returns:
        dict : A dictionary containing key-value pairs extracted from the HTML content.
    """
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        },
    )
    page = urllib.request.urlopen(req, timeout=10).read()
    parser = BeautifulSoup(page, "html.parser")
    for line in parser.find_all(["script"]):
        if "PRELOADED_STATE" in str(line.string):
            txt_line = line.string
            txt_line = txt_line.split("var PRELOADED_STATE = ")[1][:-1]
            d_line = json.loads(txt_line)
    return d_line


def ensure_unicity(list_data: list) -> list:
    """
    Ensure the uniqueness of data in a list by removing duplicate entries.

    Args:
        list_data (list): A list containing data objects with a method 'model_dump()' to represent each object as a dictionary.

    Returns:
        list: A list with duplicate entries removed, ensuring uniqueness. Each item in the list is represented as a dictionary.
    """
    df_data = pd.DataFrame.from_records([data.model_dump() for data in list_data])
    df_data = df_data.drop_duplicates()
    list_data = df_data.to_dict(orient="records")
    return list_data


def retreive_sports() -> list[WinamaxSport]:
    """
    /

    Args:
        /
    Returns:
        /
    """
    d_data: dict = parse_from_url(URL_HOME)
    sports_list: list[WinamaxSport] = [
        WinamaxSport(sport_id=str(key), sport_name=str(data["sportName"]))
        for key, data in d_data["sports"].items()
    ]
    sports_list: list[WinamaxSport] = ensure_unicity(sports_list)
    return sports_list


def retreive_matches(sports_list: list) -> list:
    """
    /

    Args:
        /
    Returns:
        /
    """
    matches_list: list[WinamaxMatch] = []
    events_list: list[WinamaxEvent] = []
    entities_list: list[WinamaxEntity] = []
    for sport in sports_list:
        url: str = URL_SPORT + sport["sport_id"]
        d_data: dict = parse_from_url(url)
        for key, match in d_data["matches"].items():
            if (match["available"]) and (str(match["sportId"]) == sport["sport_id"]):
                """
                events_list.append(
                    WinamaxEvent(
                        event_id=str('-'.join([str(match["sportId"]), str(match["categoryId"]), str(match["tournamentId"])]),
                        event_name=str('-'.join([str(match["sportId"]), str(match["sportId"]), str(match["sportId"])]),
                        sport_id=str(match["status"]),
                        category_id=str(sport["sport_id"]),
                        tournament_id=str(match["categoryId"]),
                    )
                """
                matches_list.append(
                    WinamaxMatch(
                        match_id=str(match["matchId"]),
                        match_name=str(match["title"]),
                        match_status=str(match["status"]),
                        sport_id=str(sport["sport_id"]),
                        category_id=str(match["categoryId"]),
                        tournament_id=str(match["tournamentId"]),
                    )
                )
    matches_list: list[WinamaxMatch] = ensure_unicity(matches_list)
    return matches_list


def retreive_events(d_sports: dict) -> dict:
    """
    /
    Args:
        /
    Returns:
        /
    """
    return 0


def retreive_entities() -> object:
    """
    /

    Args:
        /
    Returns:
        /
    """
    return 0


def retreive_bets() -> object:
    """
    /

    Args:
        /
    Returns:
        /
    """
    return 0


def retreive_odds() -> object:
    """
    /

    Args:
        /
    Returns:
        /
    """
    return 0


if __name__ == "__main__":
    d = retreive_sports()
    s = retreive_matches(d)
