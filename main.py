from src import widget
from src import external_api
from src.external_api import convert_to_rub

print(widget.mask_account_card('Visa Platinum 7000792289606361'))

print(widget.mask_account_card('Счет 73654108430135874305'))

print(widget.get_data('2024-03-11T02:26:18.671407'))

print(convert_to_rub('data\operations.json'))