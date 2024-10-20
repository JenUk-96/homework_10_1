from functools import wraps

from typing import Any, Union


def log(filename: Union[None, str] = None) -> Any:
    """Декоратор логирующий функции"""

    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            if filename:
                with open('log.txt', 'a', encoding='utf-8') as file:
                    try:
                        file.write(f'\nНачало работы функции {func.__name__}')
                        file.write(f'\nДокументация функции: {func.__doc__}')
                        result = func(*args, **kwargs)
                        file.write(f'\nРезультат работы функции {result}')
                        file.write('\nКонец программы')
                    except TypeError:
                        return 'Данные об ошибке: TypeError, параметры неверны\nКонец программы'
            elif not filename:
                try:
                    print('\nНачало работы функции')
                    print(f'\nДокументация функции: {func.__doc__}')
                    result = func(*args, **kwargs)
                    print(f'\nРезультат работы функции {result}')
                    print('\nКонец программы')
                except TypeError:
                    return 'Данные об ошибке: TypeError, параметры неверны'
                return result

        return inner

    return wrapper
