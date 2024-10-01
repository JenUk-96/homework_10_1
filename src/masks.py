def get_mask_card_number(card_numbers: str) -> str:
    """Функция, скрывающая номер карты"""
    card_number = str(card_numbers)
    if card_number.isdigit():
        if len(card_number) < 16:
            return ("Ошибка ввода")
        elif len(card_number) > 16:
            return "Ошибка ввода"

        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Ошибка ввода"


def get_mask_account(account_numbers: str) -> str:
    """Фунцкия, скрывающая номер банковского счета"""
    account_number = str(account_numbers)
    if account_number.isdigit():
        if len(account_number) < 20:
            return "Ошибка ввода"
        elif len(account_number) > 20:
            return "Ошибка ввода"
        return "**" + account_number[-4:]
    else:
        return "Ошибка ввода"
