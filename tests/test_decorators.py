from typing import Any

from src.decorators import log


def test_log_1() -> None:
    """Тест записи в файл"""

    @log('log.txt')
    def add(a: int, b:int) -> int:
        """Docstring"""
        return a + b

    add(3, 6)
    with open('log.txt', 'r', encoding='utf_8') as file:
        logs = file.read()
    assert 'Начало работы функции' in logs

@log()
def add_numbers(a:int, b:int) -> int:
    """Тест декоратора на сложение 2-х чисел в консоль"""
    return a + b

result = add_numbers(5, 10)
assert result == 15

def test_log_by_exception() -> None:
    '''Тест ошибки записи в файл'''
    @log('log.txt')
    def v_1(a: int, b: int) -> int:
        """Docstring"""
        return a - b

    res_1 = v_1(12, '6')
    assert res_1 == 'Данные об ошибке: TypeError, неверный формат параметров\nКонец программы'


def test_log_by_exception_2() -> None:
    '''Тестирование ошибки вывода в консоль'''

    @log()
    def v_2(a: int, b: int) -> None:
        """Docstring"""
        return a - b

    res_2 = v_2(9, '5')
    assert res_2 == 'Данные об ошибке: TypeError, неверный формат параметров'
