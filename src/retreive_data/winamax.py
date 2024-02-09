import json
import time
import urllib
import urllib.error
import urllib.request

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

URL_HOME = "https://www.winamax.fr/paris-sportifs"
URL_MATCH = "https://www.winamax.fr/paris-sportifs/match/"
URL_SPORT = "https://www.winamax.fr/paris-sportifs/sports/"
URL_BOOST = "https://www.winamax.fr/paris-sportifs/sports/100000"


def request_from_url(url: str) -> BeautifulSoup:
    """
    This function sends a request to the specified URL and returns a BeautifulSoup object representing the HTML content of the response.

    Args:
        url (str): The URL of the page to request.

    Returns:
        BeautifulSoup: A BeautifulSoup object representing the HTML content of the response to the specified URL.
    """
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        },
    )
    page = urllib.request.urlopen(req, timeout=10).read()
    parser = BeautifulSoup(page, "html.parser")
    return parser


def convert_page_to_dict(html: BeautifulSoup) -> dict[str, str]:
    """
    This function converts HTML content represented by a BeautifulSoup object into a dictionary
    containing key-value pairs extracted from the HTML.

    Args:
        html (BeautifulSoup): A BeautifulSoup object representing the HTML content to be converted.

    Returns:
        dict[str, str]: A dictionary containing key-value pairs extracted from the HTML content.
    """
    for line in html.find_all(["script"]):
        if "PRELOADED_STATE" in str(line.string):
            txt_line = line.string
            txt_line = txt_line.split("var PRELOADED_STATE = ")[1][:-1]
            d_line = json.loads(txt_line)
    return d_line


def retreive_sports() -> object:
    """
    /

    Args:
        /
    Returns:
        /
    """

    req: BeautifulSoup = request_from_url(URL_HOME)
    d_data: dict[str, str] = convert_page_to_dict(req)
    d_sports: dict[str, str] = {}
    for key, value in d_data["sports"].items():
        d_sports[key] = {}
        d_sports[key]["sport_id"] = str(key)
        d_sports[key]["sport_name"] = d_data["sports"][str(key)]["sportName"]
    df_sports = pd.DataFrame.from_dict(d_sports, orient="index")
    return df_sports


if __name__ == "__main__":
    print(retreive_sports())
