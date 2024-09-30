from typing import Any


def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> Any:
    """
    Функция принимает на вход список словарей и значение для ключа,
    возвращает новый список, в котором содержатся только те словари,
    у которых ключ содержит переданное в функцию значение.
    """

    return [d for d in list_of_dict if d.get("state") == state]


def sort_by_date(list_of_dict: list[dict], reverse: bool = True

                 ) -> list[dict]:
    """
    Функция, принимающая на вход список словарей и возвращающая новый список,
    в котором исходные словари отсортированы по убыванию даты
    """

    sorted_list = sorted(
        list_of_dict,
        key=lambda new_list_of_dict: new_list_of_dict["date"],
        reverse=reverse,
    )

    return sorted_list
