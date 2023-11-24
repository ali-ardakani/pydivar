import os
import requests
from bs4 import BeautifulSoup
import json
import tempfile
import uuid
from loguru import logger
from .info import CITY_INFORMATION

class InitialDataScraper:
    URL="https://divar.ir/s/iran"
    def __init__(self, log=None):
        self.output_folder = os.path.join(tempfile.gettempdir(), f"divar_data_{uuid.uuid4().hex[:8]}")
        os.makedirs(self.output_folder, exist_ok=True)
        self.log = log or logger

    def send_request(self):
        try:
            response = requests.get(self.URL)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            self.log.error(f"Failed to send request. Error: {e}")
            return None

    def parse_html(self, response):
        if response and response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            script_tag = soup.find('script', string=lambda text: text and 'window.__PRELOADED_STATE__' in text)
            return script_tag
        elif response:
            self.log.error(f"Failed to parse HTML. Status code: {response.status_code}")
            return None
        else:
            self.log.error("No response received for parsing HTML.")
            return None

    def extract(self, script_tag):
        if script_tag:
            raw_json = script_tag.string.partition('=')[-1].strip()
            raw_json = raw_json.split('};\n')[0] + '}'
            try:
                data = json.loads(raw_json)
                cities = data.get('multiCity', {}).get('data', {}).get('children', [])
                self.log.success("Data extracted and saved successfully.")
            except json.JSONDecodeError as e:
                self.log.error(f"Failed to decode JSON. Error: {e}")
                cities = CITY_INFORMATION
            return cities
        else:
            self.log.warning("Script tag not found.")

    def run(self):
        response = self.send_request()
        script_tag = self.parse_html(response)
        cities = self.extract(script_tag)
        
        return cities
