from errors import Error

def tokenize(expression):
    tokens = []
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isspace():
            i += 1

        if char in '+-*/':
            tokens.append(char)
            i += 1

        if char.isdigit() or char == '.':
            start = i
            dots = 0
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                if expression[i] == '.':
                    dots += 1
                    if dots > 1:
                        raise Error(f'Неправильный формат вещественного числа {expression[start:i]}')
                i += 1
            tokens.append(expression[start:i])

    return tokens


def calculate(token):
    pass