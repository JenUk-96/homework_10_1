import pytest

from src.processing import filter_by_state, sort_by_date

from tests.conftest import (list_of_dict_all_states_canceled, list_of_dict_ident_dates_sort,
                            list_of_dict_sort_res_false, list_of_dict_sort_res_true, list_of_dict_sorted_1,
                            list_of_dict_sorted_2, list_of_dict_without_state)


@pytest.fixture
def list_of_dict_fixture() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_ident_dates_fixture() -> list:
    return [
        {"id": 10243698, "state": "EXECUTED", "date": "2020-10-10T10:10:10.0"},
        {"id": 36982147, "state": "EXECUTED", "date": "2000-11-12T12:12:12.0"},
        {"id": 52148965, "state": "EXECUTED", "date": "1998-06-19T04:00:05.12"},
        {"id": 96563213, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 87458965, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
    ]


def test_filter_by_state_clasic(list_of_dict_fixture: list) -> None:
    assert filter_by_state(list_of_dict_fixture) == list_of_dict_sorted_1


def test_filter_by_state_canceled(list_of_dict_fixture: list) -> None:
    assert filter_by_state(list_of_dict_fixture, state="CANCELED") == list_of_dict_sorted_2


@pytest.mark.parametrize(
    "value, expected",
    [(list_of_dict_all_states_canceled, []), (list_of_dict_without_state, list_of_dict_without_state)],
)
def test_filter_by_state_various_input_data(value: list, expected: list) -> None:
    assert filter_by_state(value) == expected


def test_sort_by_date_clasic(list_of_dict_fixture: list) -> None:
    assert sort_by_date(list_of_dict_fixture) == list_of_dict_sort_res_true


def test_sort_by_date_rev_false(list_of_dict_fixture: list) -> None:
    assert sort_by_date(list_of_dict_fixture, reverse=False) == list_of_dict_sort_res_false


def test_sort_by_date_ident_dates(list_of_dict_ident_dates_fixture: list) -> None:
    assert sort_by_date(list_of_dict_ident_dates_fixture) == list_of_dict_ident_dates_sort
