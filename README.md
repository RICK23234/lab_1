# Toolkit

Консольная утилита на Python: **калькулятор** арифметических выражений и **конвертер** единиц измерения

## Возможности

- Калькулятор: вычисление арифметичесиких выражений: `+`, `-`, `*`, `/`, `%`, `//`. Выполняется приоритет операций (сначала `*`, `/`, `//`, `%`, потом `+` и `-`). `//` и `%` могут стоять только между целыми числами. Делить на ноль нельзя
- Конвертер длины: `m`, `mm`, `cm`, `km`
- Конвертер массы: `g`, `kg`
- Конвертер температуры: `c`, `f`, `k`

## Установка

```bash
python -m venv venv
source venv/bin/activete #Windows venv/Script/activate
pip intsall -e ".[dev]"
```

## Использование

### Калькулятор 

```bash
python -m toolkit calc "2+9"
# 11
```

### Конвертер

```bash
python -m toolkit convert 1 --from km --to m
# 1000.0
```

## Структура
```
lab/1/
├── scr/
│    └── toolkit/
│        ├── __init__.py
│        ├── __main__.py
│        ├── calculator.py
│        ├── converter.py
│        └── error.py
│
├── tests/
│    ├── calculator_test.py
│    ├── converter_test.py
│    └── cli_test.py
├── pyproject.toml
└── README.md

```

## Тесты и линтер
```bash
python -m pytest
ruff check .
```

