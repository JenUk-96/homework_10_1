from typing import Any

import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("") == "Ошибка ввода"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("4276060032300678000000000", "Ошибка ввода"),
        ("zhyenkfudjlpdoiu", "Ошибка ввода"),
        ("1l4.dlg8pr-a8]6m", "Ошибка ввода"),
        ("4276060032300", "Ошибка ввода"),
        ("", "Ошибка ввода"),
    ],
)
def test_get_mask_card_number_various_input_data(value: Any, expected: Any) -> Any:
    return get_mask_card_number(value) == expected


def test_get_mask_account() -> None:
    assert get_mask_account("01234567890123456789") == "**6789"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("0123456789", "Ошибка ввода"),
        ("asdfasf21321321", "Ошибка ввода"),
        ("", "Ошибка ввода"),
        ("asdnajdfaskdvkas", "Ошибка ввода")
    ],
)
def test_get_mask_account_various_input_data(value: Any, expected: Any) -> Any:
    return get_mask_account(value) == expected
