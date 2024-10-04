from src.widget import mask_account_card

from src.widget import get_data

import pytest


def test_mask_account_card() -> None:
    assert mask_account_card("") == "Ошибка ввода"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum  1234 56** **** 3456"),
        ("Счет 01234567890123456789", "Счет  **6789"),
        ("Счет", "Ошибка ввода"),
        ("Master Card 4569873210852036", "Master Card  4569 87** **** 2036"),
        ("Master", "Ошибка ввода"),
        ("cxtb 12345678901234567890", "Ошибка ввода")
    ],
)
def test_mask_account_card_various_input_data(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


def test_get_data() -> None:
    assert get_data("2018-10-14T08:21:33.419441") == "14.10.2018"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2020-10-10T10:10:10.0", "10.10.2020"),
        ("2000-11-12T12:12:12.0", "12.11.2000"),
        ("1998-06-19T04:00:05.12", "19.06.1998"),
        ("T06:15:09.321456", "Не корректный ввод даты"),
        ("02024-10-12T02:29:19.258963", "Не корректный ввод даты")
    ],
)
def test_get_data_various_input_data(value: str, expected: str) -> None:
    assert get_data(value) == expected
