def get_mask_card_number(card_numbers: str) -> str:
    """Функция, скрывающая номер карты"""
    card_number = str(card_numbers)

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_numbers: str) -> str:
    """Фунцкия, скрывающая номер банковского счета"""
    account_number = str(account_numbers)
    return "**" + account_number[-4:]
