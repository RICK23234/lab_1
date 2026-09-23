import pytest

from scr.toolkit.converter import convert
from scr.toolkit.errors import *


def test_from_m_to_cm():
    assert convert(1, "m", "cm") == 100.0


def test_from_m_to_km():
    assert convert(2, "m", "km") == 0.002


def test_from_c_to_f():
    assert convert(6, "c", "f") == 42.8


def test_from_c_to_k():
    assert convert(10, "c", "k") == 283.15


def test_from_f_to_k():
    assert convert(5, "f", "k") == 258.15


def test_from_kg_to_g():
    assert convert(7, "kg", "g") == 7000.0


def test_absolute_zero():
    assert convert(-273.15, "c", "k") == 0.0


def test_below_absolute_zero_raises():
    with pytest.raises(BelowAbsoluteZeroError):
        convert(-350, "c", "k")


def test_incompatible_units_raises():
    with pytest.raises(IncompatibleUnitsError):
        convert(80, "km", "kg")


def test_unknown_unit_raises():
    with pytest.raises(UnknownUnitError):
        convert(65, "gh", "km")
