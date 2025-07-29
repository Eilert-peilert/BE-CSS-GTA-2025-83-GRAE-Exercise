import pytest
from helper_functions import parse_json_data


def test_parse_country_names_valid_json():
    json_str = """
    [
        {"name": "Brazil"},
        {"name": "Canada"},
        {"name": "Australia"}
    ]
    """
    expected = ["Australia", "Brazil", "Canada"]
    assert parse_json_data(json_str) == expected
