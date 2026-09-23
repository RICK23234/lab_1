from .errors import (
    DivisionZeroError,
    EmptyExpressionError,
    FormatExpressionError,
    FormatFloatError,
    FormatNumError,
    MissingNumberError,
    MissingOperatorError,
)


def tokenize(expression: str) -> list:
    """
    Функция для токенизации выражения ('1+3-4/6.0' -> ['1' '+' '3' '-' '4' '/' '6.0'])
    """
    tokens = []
    i = 0

    while i < len(expression):
        char = expression[i]

        if char not in "+-*/" and char.isdigit() == 0 and char.isspace() == 0:
            raise FormatExpressionError(char)

        if char.isspace():
            i += 1

        if char in "+-*/":
            tokens.append(char)
            i += 1

        if char.isdigit() or char == ".":
            start = i
            dots = 0
            while i < len(expression) and (
                expression[i].isdigit() or expression[i] == "."
            ):
                if expression[i] == ".":
                    dots += 1
                i += 1
            if dots > 1:
                raise FormatFloatError(expression[start:i])
            tokens.append(expression[start:i])

    return tokens


def calculate(analyzed: list) -> int:
    """
    Функция для вычисления введеного выражения
    """
    expression = [analyzed[0]]
    i = 1
    while i < len(analyzed):  # по приоретету операций сначала вычисляем * и /
        operetor = analyzed[i]
        num = analyzed[i + 1]

        if operetor == "*":
            expression[-1] = expression[-1] * num
        elif operetor == "/":
            if num == 0:
                raise DivisionZeroError()
            expression[-1] = expression[-1] / num
        else:
            expression.append(operetor)
            expression.append(num)

        i += 2

    res = expression[0]
    i = 1
    while i < len(
        expression
    ):  # после умножения и деления вычисляем сложение и вычитание
        operetor = expression[i]
        num = expression[i + 1]

        if operetor == "+":
            res += num
        else:
            res -= num

        i += 2

    return res


def validation(tokens: list) -> list:
    """
    Функция для валидации токенов, поиска унарных минусов
    """
    if not tokens:
        raise EmptyExpressionError()

    validated = []
    i = 0

    while i < len(tokens):
        sign = 1  # знак числа
        while i < len(tokens) and tokens[i] in "+-":
            if tokens[i] == "-":
                sign *= -1  # если минус, как унaрный знак, то меняем знак числа
            i += 1

        # проверяем что не вышли за переделы списка и что следущий токен число
        if i >= len(tokens) or tokens[i] in "+-*/":
            raise MissingNumberError()

        num_token = tokens[i]
        if len(num_token) >= 2 and num_token[0] == "0" and num_token[1] != ".":
            raise FormatNumError(num_token)

        if "." in num_token:
            num = float(num_token)
        else:
            num = int(num_token)
        validated.append(num * sign)
        i += 1

        if i >= len(tokens):
            break  # если после добавления числа в список конец выражения то выходим из цикла

        if tokens[i] not in ("+-*/"):
            raise MissingOperatorError()

        validated.append(tokens[i])
        i += 1

    if validated[-1] in ("-", "+", "*", "/"):
        raise MissingNumberError()

    return validated


def calculate_expression(expression: str) -> int | float:
    """
    Функия для объединения функций tokenize, analize, calculate
    """
    tokens = tokenize(expression)
    validated = validation(tokens)
    return calculate(validated)
