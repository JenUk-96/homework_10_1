from datetime import datetime

from src.csv_reader import read_transactions_pd, file_path_csv
from src.pandas_reader import read_transactons_xtml, path_file_xlsx
from src.processing import filter_by_state, sort_by_date
from src.utils import path_file_json, financial_transactions
from src.widget import mask_account_card


def main():
    """Отвечает за основную логику проекта с пользователем и связывает функциональности между собой."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    print("""Выберите необходимый пункт меню:
    \n1. Получить информацию о транзакциях из JSON-файла
    \n2. Получить информацию о транзакциях из CSV-файла
    \n3. Получить информацию о транзакциях из XLSX-файла 
    \n""")
    user_input_num = input()

    if user_input_num == "1":
        transactions_file = financial_transactions(path_file_json)
        print("Для обработки выбран JSON-файл.")
    elif user_input_num == "2":
        transactions_file = read_transactions_pd(file_path_csv)
        print("Для обработки выбран CSV-файл.")
    elif user_input_num == "3":
        transactions_file = read_transactons_xtml(path_file_xlsx)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Некорректный пункт меню")
        return

    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        user_input_st = input("Выбирите необходимый статус:\n").lower()
        if user_input_st != 'executed' and user_input_st != 'canceled' and user_input_st != 'pending':
            print(f"Статус операции {user_input_st} недоступен")
            continue
        print(f'Операции отсортированы по статусу {user_input_st}')
        state_filter = filter_by_state(transactions_file, user_input_st)
        break
    print("Отсортировать операции по дате? Да/Нет")
    user_input_date = input().lower()
    if user_input_date == 'да':
        print('Отсортировать по возрастанию или по убыванию?')
        user_input_up_down = input('в порядке возрастания / в порядке убывания').lower()
        if user_input_up_down == 'в порядке возравстания' or user_input_up_down == 'по возрастанию':
            reversed = False
            filter_transactions_date = sort_by_date(state_filter, reversed)
        elif user_input_up_down == 'в порядке убывания' or 'по убыванию':
            reversed = True
            filter_transactions_date = sort_by_date(state_filter, reversed)
        else:
            print('Нет такого варианта')
        return
    elif user_input_date == 'нет':
        filter_transactions_date = state_filter
    else:
        print('Нет такого варианта.')
        return

    print('Выводить только рублевые(RUB) трансакции: Да/Нет?')
    user_input_currency = input('Введите ответ: Да/Нет\n').lower()
    if user_input_currency == 'да':
        rub_transfer = []
        for trans in filter_transactions_date:
            if user_input_num == '1' or user_input_num == '2':
                if trans['operationAmount']['currency']['code'] == 'RUB':
                    rub_transfer.append(trans)
            else:
                if trans['currency_code'] == 'RUB':
                    rub_transfer.append(trans)
    elif user_input_currency == 'нет':
        rub_transfer = []
        for trans in filter_transactions_date:
            rub_transfer.append(trans)
    else:
        print('Введен некорректный ответ.')
        return

    print('Отфильтровать список трансакций по определенному слову в описании: Да/Нет?')
    user_input_filter = input('Введите ответ:\n').lower()
    if user_input_filter == 'да':
        filter_by_word_yes = input('Введите слово для фильтрации:')
        filters_words = []
        for trans in rub_transfer:
            if filter_by_word_yes in trans['discriptions']:
                filters_words.append(trans)
    elif user_input_filter == 'нет':
        filter_words = []
        for trans in rub_transfer:
            filter_words.append(trans)
    else:
        print('Введен некорректный ответ.')
        return
    if len(filters_words) == 0:
        print('По вашему слову не найдено ни одной транзакции.')
        return

    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(filters_words)}\n')

    for trans in filters_words:
        if trans.get('from') and trans.get('to'):
            date = trans.get("date", "")[:19]
            bad_time = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
            correct_date = bad_time.strptime("%d.%m.%Y")
            description = trans.get("descriptions", "")
            mask_card_from = mask_account_card(str(trans.get("from")))
            mask_card_to = mask_account_card(str(trans.get("to")))
            mask_acc_from = mask_account_card(str(trans.get("from")))
            mask_acc_to = mask_account_card(str(trans.get("to")))
            if user_input_num == '1':
                amount = trans["operationAmount"]["amount"]
                if "Счет" in trans.get("from", "") and "Счет" in trans.get("to", ""):
                    print(f'{correct_date} {description}')
                    print(f'{mask_acc_from} -> {mask_acc_to}')
                    if trans.get("code") == "RUB":
                        print("Сумма: {amount} руб. \n")
                    else:
                        print(f'Сумма: {amount} {trans["operationAmount"]["code"]}\n')
                elif "Счет" in trans.get("to", ""):
                    print(f'{correct_date} {description}')
                    print(f'Счет: {mask_acc_to}')
                    if trans.get("code") == "RUB":
                        print(f'Сумма: {amount} руб.\n')
                    else:
                        print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')
                else:
                    print(f'{correct_date} {description}')
                    print(f"Транзакция: {mask_card_from} -> {mask_card_to}")
                    if trans.get("code") == 'RUB':
                        print(f'Сумма: {amount} руб.\n')
                    else:
                        print(f'Сумма {amount} {trans["operationsAmount"]["currency"]["code"]}\n')
            else:
                amount = trans["amount"]
                if "Счет" in str(trans.get("from")) and "Счет" in str(trans.get("to")):
                    print(f"{correct_date} {description}")
                    print(f"Счет: {mask_acc_from} -> Счет: {mask_acc_to}")
                    if trans.get("code") == "RUB":
                        print(f"Сумма: {amount} руб.\n")
                    else:
                        print(f'Сумма: {amount} {trans["currency_code"]}\n')
                elif "Счет" in trans.get("to", ""):
                    print(f"{correct_date} {description}")
                    print(f"Счет: {mask_acc_to}")
                    if trans.get("to") == "RUB":
                        print(f'Сумма: {amount} руб.\n')
                    else:
                        print(f'Сумма: {amount} {trans["currency_code"]}\n')
                else:
                    print(f'{correct_date} {description}')
                    print(f'Тразакция: {mask_card_from} -> {mask_card_to}')
                    if trans.get("code") == "RUB":
                        print(f"Сумма: {amount} руб.")
                    else:
                        print(f'Сумма: {amount} {trans["currency_code"]}\n0')


if __name__ == "__main__":
    main()
