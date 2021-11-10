import scrapy
from bs4 import BeautifulSoup
import urllib
import urllib.error
import urllib.request
import json
import pandas as pd
import numpy as np
import time


class WinamaxSpider(scrapy.Spider):
    name = 'winamax'
    allowed_domains = ['winamax.fr']
    URL_HOME = 'https://www.winamax.fr/paris-sportifs/'
    URL_MATCH = 'https://www.winamax.fr/paris-sportifs/match/'
    URL_SPORT = 'https://www.winamax.fr/paris-sportifs/sports/'
    URL_BOOST = 'https://www.winamax.fr/paris-sportifs/sports/100000'

    def request_get_html(self, url):
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        )   
        page = urllib.request.urlopen(req, timeout=10).read()
        parser = BeautifulSoup(page, 'html.parser')
        return parser

    def winamax_get_dict_script_data(self, html):
        for line in html.find_all(['script']):
            if "PRELOADED_STATE" in str(line.string):
                txt_line = line.string
                txt_line = txt_line.split('var PRELOADED_STATE = ')[1][:-1]
                d_line = json.loads(txt_line)
        return d_line

    def winamax_get_mapping_sport(self, html):
        req = self.request_get_html(html)
        d_data = self.winamax_get_dict_script_data(req)
        d_mapping_sport = {}
        for k in d_data['sports']:
            d_mapping_sport[k] = d_data['sports'][str(k)]['sportName']
        d_mapping_sport_reverse = {v: k for k, v in d_mapping_sport.items()}
        return d_mapping_sport, d_mapping_sport_reverse
    

    def start_requests(self):
        SCOPE_SPORTS = ['Football', 'Basketball', 'Baseball', 'Tennis']
        d_mapping_sport, d_mapping_sport_reverse = self.winamax_get_mapping_sport(self.URL_HOME)
        req = self.request_get_html(self.URL_HOME)
        d_data = self.winamax_get_dict_script_data(req)
        SCOPE_SPORTS = list(set(SCOPE_SPORTS) & set(d_mapping_sport_reverse.keys()))
        for label_sport in SCOPE_SPORTS:
            id_sport = d_mapping_sport_reverse[label_sport]
            url = self.URL_SPORT + str(id_sport)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        print("1")     
        print(response)
        self.logger.info('A response from %s just arrived!', response.url)