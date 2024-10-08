from functools import wraps

from typing import Any, Union


def log(filename: Union[None, str] = None) -> Any:
    """Декоратор логирующий функции"""

    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args, **kwargs: Any) -> Any:
            if filename:
                with open('log.txt', 'a', encoding='utf-8') as file:
                    try:
                        file.write(f'\nНачало работы функции {func.__name__}')
                        file.write((f'\nДокументация функции {func.__doc__}'))
                        start = func(*args, **kwargs)
                        file.write(f'\nРезультат работы функции {start}')
                        file.write(f'\nКонец работы функции')
                    except TypeError:
                        return 'Данные об ошибке: TypeError, неверный формат параметров\nКонец программы'
            elif not filename:
                try:
                    print('\nНачало работы функции {func.__name__}')
                    print('\nДокументация функции {func.__name__')
                    start = func(*args, **kwargs)
                    print('\nРезультат работы функции {start}')
                    print('\nКонец работы функции')
                except TypeError:
                    return 'Данные об ошибке: TypeError, неверный формат параметров'
                return start
        return inner
    return wrapper
