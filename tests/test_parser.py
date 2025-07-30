import pytest
import json
from country_picker.helper_functions import parse_json_data


def test_parse_country_names_valid_json():
    country_list = [
        {"name": "Brazil"},
        {"name": "Canada"},
        {"name": "Australia"}
    ]
    json_str = json.dumps(country_list)
    expected = ["Australia", "Brazil", "Canada"]
    assert parse_json_data(json_str) == expected


def test_parse_country_names_missing_field():
    country_list = [
        {"wrong": "value"},
        {"name": "Norway"}
    ]
    json_str = json.dumps(country_list)
    assert parse_json_data(json_str) == ["Norway"]


def test_parse_country_names_empty_list():
    country_list = []
    json_str = json.dumps(country_list)
    assert parse_json_data(json_str) == []


def test_parse_country_names_invalid_json():
    with pytest.raises(Exception):
        parse_json_data("invalid-json")
