from src import masks


# types_of_cars = ["Visa Electron", "Visa Classic", "Visa Gold", "Visa Platinum",
#                 "MasterCard Cirrus", "MasterCard Maestro", "MasterCard Standard",
#                "MasterCard Gold", "MasterCard Platinum"]


def mask_account_card(account_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    count_number = ""
    name_card = ""
    for element in account_card:
        if element.isdigit():
            count_number += str(element)
        else:
            name_card += str(element)
    if len(count_number) == 0:
        return "Ошибка ввода"
    elif len(count_number) == 16 or len(count_number) == 20:
        if len(count_number) == 16:
            # if name_card in types_of_cars:
            #    name_card ==
            card_mask = masks.get_mask_card_number(count_number)
            return f"{name_card} {card_mask}"
        elif len(count_number) == 20 and name_card == "Счет ":
            account_mask = masks.get_mask_account(count_number)
            return f"{name_card} {account_mask}"
        else:
            return "Ошибка ввода"
    else:
        return "Ошибка ввода"


def get_data(user_date: str) -> str:
    """Функция принимающая строку даты и выводящая дату в формате дд.мм.гггг"""
    if type(user_date) != str:
        return "Не корректный ввод даты"

    if 20 < len(user_date) < 27:
        user_data_slace = user_date[0:10]
        revers_user_data = f"{user_data_slace[-2::1]}.{user_data_slace[-5:-3]}.{user_data_slace[0:4]}"

        return revers_user_data
    else:
        return "Не корректный ввод даты"
