import csv
import os.path

import pandas as pd

file_path_csv = os.path.join(os.path.abspath(__file__), '../../data/transactions.csv')

def read_transactions_dict(file_path: str) -> list:
    transactions = []
    """Функция, которая принимает путь к файлу csv, и выдает список словарей с транзакциями"""
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
        return transactions
    except FileNotFoundError:
        return []


def read_transactions_func(file_path: str) -> list:
    """Функция, которая принимает пусть к файлу csv, и читает файл"""
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        return []


def read_transactions_pd(file_path: str) -> list:
    """Функция, которая принимает путь к файлу csv, и выдает список словарей с тразакциями"""
    try:
        transactions = pd.read_csv(file_path)
        transactions_dict = transactions.to_dict(orient='records')
        return transactions_dict
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    file_path_csv = os.path.join(os.path.abspath(__file__), '../../data/transactions.csv')
    transactions = read_transactions_dict(file_path)
    print(transactions)
