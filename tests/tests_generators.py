import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions_generator: list, empty_lsts: list) -> None:
    usd_transactions_with_currency = filter_by_currency(transactions_generator, 'USD')
    assert next(usd_transactions_with_currency) == {
                                        "id": 939719570,
                                        "state": "EXECUTED",
                                        "date": "2018-06-30T02:08:58.425572",
                                        "operationAmount": {
                                            "amount": "9824.07",
                                            "currency": {
                                                "name": "USD",
                                                "code": "USD"
                                            }
                                        },
                                        "description": "Перевод организации",
                                        "from": "Счет 75106830613657916952",
                                        "to": "Счет 11776614605963066702"
                                    }

    assert next(usd_transactions_with_currency) == {
                                        "id": 142264268,
                                        "state": "EXECUTED",
                                        "date": "2019-04-04T23:20:05.206878",
                                        "operationAmount": {
                                            "amount": "79114.93",
                                            "currency": {
                                                "name": "USD",
                                                "code": "USD"
                                            }
                                        },
                                        "description": "Перевод со счета на счет",
                                        "from": "Счет 19708645243227258542",
                                        "to": "Счет 75651667383060284188"
                                    }

    with pytest.raises(StopIteration):
        usd_transactions_wo_currency = filter_by_currency(transactions_generator, '')
        assert next(usd_transactions_wo_currency)

    with pytest.raises(StopIteration):
        usd_transactions_wo_currency = filter_by_currency(transactions_generator, 'EUR')
        assert next(usd_transactions_wo_currency)

    with pytest.raises(StopIteration):
        usd_transaction_empty_lst = filter_by_currency(empty_lsts, "USD")
        assert next(usd_transaction_empty_lst)


def test_transaction_descriptions(transactions_generator: list, empty_lsts: list, ) -> None:
    descriptions = transaction_descriptions(transactions_generator)
    assert next(descriptions) == "Перевод организации"

    assert next(descriptions) == "Перевод со счета на счет"
    with pytest.raises(StopIteration):
        descriptions_empy_lst = transaction_descriptions(empty_lsts)
        assert next(descriptions_empy_lst)


@pytest.mark.parametrize('start, stop, result', [
    (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']),
    (2589632, 2589634, ['0000 0000 0258 9632', '0000 0000 0258 9633', '0000 0000 0258 9634']),
    (9876543210987654, 1478963225877412, ['']),
    (1234567890123456, 12341234123412352, ['']),
    ('32214', '987546', ['']),
    (10, 9, [''])
                                                ])
def test_card_number_generator(start: int, stop: int, result: list) -> None:
    generator_card = list(card_number_generator(start, stop))
    assert generator_card == result
