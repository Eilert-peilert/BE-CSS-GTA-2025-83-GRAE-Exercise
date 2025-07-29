import json
import urllib.request
from typing import List

def fetch_country_names() -> List[str]:
    url = "https://www.apicountries.com/countries"
    with urllib.request.urlopen(url) as response:
        raw_json_data = response.read().decode("utf-8")
        return parse_json_data(raw_json_data)


def parse_json_data(json_str: str) -> List[str]:
    data = json.loads(json_str)
    country_names = [item["name"] for item in data if "name" in item]
    return sorted(country_names)