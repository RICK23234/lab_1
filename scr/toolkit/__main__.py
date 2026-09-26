import sys
from argparse import ArgumentParser

from .calculator import calculate_expression
from .converter import convert
from .errors import Error, FormatNumError


def build():
    parser = ArgumentParser(prog="toolkit", description="Калькулятор и конвертер")
    subparsers = parser.add_subparsers(dest="command", required=True)

    calc_parser = subparsers.add_parser(name="calc", help="вычислить выражение", prefix_chars="~")
    calc_parser.add_argument("expression")

    convert_parser = subparsers.add_parser(name="convert", help="конвертер")
    convert_parser.add_argument("value")
    convert_parser.add_argument("--from", dest="from_unit", required=True)
    convert_parser.add_argument("--to", dest="to_unit", required=True)

    return parser


def run_calcu(arg):
    res = calculate_expression(arg.expression)
    print(res)


def run_convert(arg):
    try:
        num = float(arg.value)
    except ValueError:
        raise FormatNumError(arg.value)

    res = convert(num, arg.from_unit, arg.to_unit)
    print(res)


def main(arg=None):
    parser = build()
    arguments = parser.parse_args(arg)

    try:
        if arguments.command == "calc":
            run_calcu(arguments)
        elif arguments.command == "convert":
            run_convert(arguments)
    except Error as error:
        print(f"\033[1;91mОшибка: {error} \033[0m", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    main()
