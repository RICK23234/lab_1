from .errors import BelowAbsoluteZeroError, IncompatibleUnitsError, UnknownUnitError

# словарь хранения наименований единиц измерения длины и их значение
# относительно единицы СИ (в метрах)
lenth = {"km": 1000.0, "m": 1.0, "cm": 0.01, "mm": 0.001}
# словарь хранения наименовний единиц измерения массы и их значения
# относительно единицы СИ (килограммы)
mass = {"kg": 1.0, "g": 0.001}
# кортеж хранения наименований единиц измерений температуры
temp = ("c", "f", "k")

absolute_zero_in_celsia = -273.15  # значение абсолютного нуля в Цельсиях


def to_celsia(temp: float, unit: str) -> float:
    """
    Функция перевода из любой единицы измерения температуры в Цельсию
    """
    if unit == "c":
        res = temp  # из Цельсия в Цельсию
    if unit == "k":
        res = temp - 273.15  # из кельвина в цельсию
    if unit == "f":
        res = (temp - 32) * 5 / 9  # из Фаренгейтов и Цельсию

    if res < absolute_zero_in_celsia:
        # если итоговая температура ниже абсолютого нуля то ошибка
        raise BelowAbsoluteZeroError()

    return res


def from_celsia(temp: float, unit: str) -> float:
    """
    Функция перевода из цельсия в любую единицу измерения температуры
    """
    if unit == "c":
        res = temp  # из Цельсии в Цельсию
    if unit == "k":
        res = temp + 273.15  # из Цельсии в Кельвин
    if unit == "f":
        res = temp * 9 / 5 + 32  # из Цельсии в Фаренгейты

    return res


def detemine_group(unit: str) -> str:
    """
    Функция для определения группы единицы измерения (масса, длина, температура)
    """
    if unit in mass:
        return "mass"
    if unit in lenth:
        return "lenth"
    if unit in temp:
        return "temp"
    return None


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Функция для конвертации всех единиц измерения (массы, длины, температуры)
    """
    from_group = detemine_group(from_unit.lower())
    to_group = detemine_group(to_unit.lower())

    if from_group is None:
        raise UnknownUnitError(from_unit)
    if to_group is None:
        raise UnknownUnitError(to_unit)
    if from_group != to_group:
        raise IncompatibleUnitsError(from_unit, to_unit)

    if from_group == "mass":
        res = value * mass[from_unit] / mass[to_unit]
    elif from_group == "lenth":
        res = value * lenth[from_unit] / lenth[to_unit]
    else:
        res = from_celsia(to_celsia(value, from_unit), to_unit)

    return res
