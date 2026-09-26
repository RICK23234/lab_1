class Error(Exception):
    pass


class FormatFloatError(Error):
    def __init__(self, num: float) -> None:
        super().__init__(f'Недопустимый формат вещественного числа "{num}"')


class FormatNumError(Error):
    def __init__(self, num) -> None:
        super().__init__(f'Неверный формат числа {num}')


class FormatExpressionError(Error):
    def __init__(self, token: str) -> None:
        super().__init__(f'{token} не явялется ни числом, ни знаком')


class EmptyExpressionError(Error):
    def __init__(self) -> None:
        super().__init__('Пустое выражение')


class MissingNumberError(Error):
    def __init__(self) -> None:
        super().__init__('Пропущено число')


class MissingOperatorError(Error):
    def __init__(self) -> None:
        super().__init__('Пропущен знак')


class DivisionZeroError(Error):
    def __init__(self) -> None:
        super().__init__('Деление на ноль')


class BelowAbsoluteZeroError(Error):
    def __init__(self) -> None:
        super().__init__('Температура ниже абсолютного нуля (-273.15 °C)')


class UnknownUnitError(Error):
    def __init__(self, unit: str) -> None:
        super().__init__(f'Неизвестная единица измерения "{unit}"')


class IncompatibleUnitsError(Error):
    def __init__(self, unit1: str, unit2: str) -> None:
        super().__init__(f'Несовместимые единицы измерения "{unit1}" и "{unit2}"')


class UnknownCommandError(Error):
    def __init__(self, comm) -> None:
        super().__init__(f'Неизвестная команда {comm}')
