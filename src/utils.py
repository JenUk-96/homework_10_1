import json
import logging
import os.path
from json import JSONDecodeError
from pathlib import Path
from typing import Any

from src.external_api import currency_conversion

path_file_json = os.path.join(os.path.abspath(__file__), '../../data/operations.json')

# logging.basicConfig(
#    level=logging.INFO,
#   format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
#    filename="../logs/utils.log",
#    filemode="w", encoding='utf-8'
# )
PATH_TO_PROJECT = Path(__file__).resolve().parent.parent
PATH_TO_FILE = PATH_TO_PROJECT / "data" / "operations.json"

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler(PATH_TO_PROJECT / "logs" / "utils.log", encoding="UTF-8", mode="w")
fileFormatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fileHandler.setFormatter(fileFormatter)
logger.addHandler(fileHandler)

financial_transactions_logger = logging.getLogger()
transaction_amount_logger = logging.getLogger()


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о
     финансовых транзакциях."""
    try:
        financial_transactions_logger.info(f"Получение данных из файла {path}")
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                financial_transactions_logger.error("Ошибка файла с транзакциями")
                return []
        if not isinstance(transactions, list):
            financial_transactions_logger.error("Список транзакций пуст")
            return []
        financial_transactions_logger.info("Создан список словарей с данными о финансовых транзакциях")
        return transactions
    except FileNotFoundError:
        financial_transactions_logger.error("Файл с транзакциями не найден")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        transaction_amount_logger.info("Код валюты в транзакции RUB")
    else:
        amount = currency_conversion(trans)
        transaction_amount_logger.info("Код валюты транзакции не RUB, произведена конвертация")
    return amount


print(financial_transactions('operations.json'))


