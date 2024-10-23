import csv
import os.path

import pandas as pd


def read_transactions_dict(file_path: str) -> list:
    transactions = []
    """Функция, которая принимает путь к файлу csv"""
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions


def read_transactions_func(file_path: str) -> list:
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def read_transactions_pd(file_path: str) -> list:
    transactions = pd.read_csv(file)



if __name__ == '__main__':
    file_path = os.path.join(os.path.abspath(__file__), '../../data/transactions.csv')
    transactions = read_transactions_dict(file_path)
    print(transactions)
