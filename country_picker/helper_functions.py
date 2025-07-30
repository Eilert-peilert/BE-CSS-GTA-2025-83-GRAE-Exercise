import json
import urllib.request
from typing import List
from PyQt6.QtCore import QObject, pyqtSignal

class CountryFetcher(QObject):
    error = pyqtSignal(str)

    def run(self) -> List[str]:
        try: 
            url = "https://www.apicountries.com/countries"
            with urllib.request.urlopen(url) as response:
                raw_json_data = response.read().decode("utf-8")
                return parse_json_data(raw_json_data)
        except Exception as e:
            self.error.emit(str(e))


def parse_json_data(json_str: str) -> List[str]:
    data = json.loads(json_str)
    country_names = [item["name"] for item in data if "name" in item]
    return sorted(country_names)