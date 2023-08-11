"""
Информация получена:
https://pythonist.ru/bystraya-sortirovka-na-python/
"""


def input_int(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Ошибка! Необходимо ввести целое число!')


def input_float(message: str) -> any([int, float]):
    while True:
        user_input = input(message)
        try:
            res = float(user_input)
            try:
                res = int(user_input)
            finally:
                return res
        except ValueError:
            print('Ошибка! Необходимо ввести число!')
