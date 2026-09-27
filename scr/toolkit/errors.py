"""Исключения для калькулятора и конвертора"""


class Error(Exception):
    """Базовое исключения для всех ошибок"""
    pass


class FormatFloatError(Error):
    """Вещественное число указано в неправильном формате"""

    def __init__(self, num: float) -> None:
        super().__init__(f'Недопустимый формат вещественного числа "{num}"')


class FormatNumError(Error):
    """Число указано в недопустимом формате"""

    def __init__(self, num) -> None:
        super().__init__(f'Неверный формат числа {num}')


class FormatExpressionError(Error):
    """В выражении символ, которые не является ни числом, ни знаком """

    def __init__(self, token: str) -> None:
        super().__init__(f'{token} не явялется ни числом, ни знаком')


class EmptyExpressionError(Error):
    """Введено пустое выржание"""

    def __init__(self) -> None:
        super().__init__('Пустое выражение')


class MissingNumberError(Error):
    """В выражении пропущено число"""

    def __init__(self) -> None:
        super().__init__('Пропущено число')


class MissingOperatorError(Error):
    """В выражении пропущен знак"""

    def __init__(self) -> None:
        super().__init__('Пропущен знак')


class DivisionZeroError(Error):
    """Попытка деления на ноль"""

    def __init__(self) -> None:
        super().__init__('Деление на ноль')


class IntOperatorsError(Error):
    """// или % стоит между не целыми числами"""

    def __init__(self, operator):
        super().__init__(f'{operator} может стоять только между двуми целыми числами')

        
class BelowAbsoluteZeroError(Error):
    """Введенная температура ниже абсолютного нуля"""

    def __init__(self) -> None:
        super().__init__('Температура ниже абсолютного нуля (-273.15 °C)')


class UnknownUnitError(Error):
    """Указана единица измерения, неизвестная конвертору"""

    def __init__(self, unit: str) -> None:
        super().__init__(f'Неизвестная единица измерения "{unit}"')


class IncompatibleUnitsError(Error):
    """Указанные единицы измерения относятся к разным группам"""

    def __init__(self, unit1: str, unit2: str) -> None:
        super().__init__(f'Несовместимые единицы измерения "{unit1}" и "{unit2}"')
        