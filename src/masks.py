import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filename="../logs/masks.log",
    filemode="w", encoding='utf-8'
)
card_number_logger = logging.getLogger()
mask_account_logger = logging.getLogger()

if __name__ == "__main__":

    def get_mask_card_number(card_numbers: str) -> str:
        """Функция, скрывающая номер карты"""
        card_number_logger.info("Создаю маску номера карты")
        card_number = str(card_numbers)
        if card_number.isdigit():
            if len(card_number) < 16:
                card_number_logger.error("Неправильный номер карты")
                return "Ошибка ввода"
            elif len(card_number) > 16:
                card_number_logger.error("Неправильный номер карты")
                return "Ошибка ввода"
            card_number_logger.info("Маска номера карты создана")
            return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        else:
            return "Ошибка ввода"

    def get_mask_account(account_numbers: str) -> str:
        """Фунцкия, скрывающая номер банковского счета"""
        mask_account_logger.info("Создаю маску номера счета")
        account_number = str(account_numbers)
        if account_number.isdigit():
            if len(account_number) < 20:
                mask_account_logger.error("Неправильный номер счета")
                return "Ошибка ввода"
            elif len(account_number) > 20:
                mask_account_logger.error("Неправильный номер счета")
                return "Ошибка ввода"
            mask_account_logger.info("Маска номера счета создана")
            return "**" + account_number[-4:]
        else:
            return "Ошибка ввода"

    print(get_mask_card_number('0123456789012345'))
    print(get_mask_card_number('123'))
    print(get_mask_account('01234567890123456789'))
    print(get_mask_account('0258'))
