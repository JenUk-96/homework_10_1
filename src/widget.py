from src import masks


def mask_account_card(account_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    count_number = ""
    name_card = ""

    for element in account_card:
        if element.isdigit():
            count_number += str(element)
        else:
            name_card += str(element)
    if len(count_number) == 16:
        card_mask = masks.get_mask_card_number(count_number)
        return f"{name_card} {card_mask}"
    elif len(count_number) == 20:
        account_mask = masks.get_mask_account(count_number)
        return f"{name_card} {account_mask}"


print(mask_account_card("Счет 73654108430135874305"))


def get_date(user_date: str) -> str:
    """Функция принимающая строку даты и выводящая дату в формате дд.мм.гггг"""
    user_data_slace = user_date[0:10]
    revers_user_data = f"{user_data_slace[-2::1]}. {user_data_slace[-5:-3]}. {user_data_slace[0:4]}"

    return revers_user_data
