"""Line/code coverage tests for airline_baggage.py.

Run from this directory with:
    python -m coverage run --source=airline_baggage -m pytest -q CodeCoverageTest_airline_baggage.py
    python -m coverage report -m
"""
import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


@pytest.mark.parametrize("cabin,allowance", [
    ("economy", 15), ("premium", 25), ("business", 40),
])
def test_each_cabin_within_allowance(cabin, allowance):
    assert baggage_fee(cabin, allowance, "domestic", False) == 0


def test_unknown_cabin_raises():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 10, "domestic", False)


def test_negative_weight_raises():
    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -0.1, "domestic", False)


def test_member_allowance_for_non_business():
    assert baggage_fee("economy", 20, "domestic", True) == 0


def test_business_member_does_not_get_extra_allowance():
    assert baggage_fee("business", 41, "domestic", True) == 20


def test_domestic_excess_fee():
    assert baggage_fee("economy", 16, "domestic", False) == 20


def test_international_excess_fee():
    assert baggage_fee("economy", 16, "international", False) == 45


def test_large_domestic_excess_doubles_rate():
    assert baggage_fee("economy", 36, "domestic", False) == 840


def test_large_international_excess_doubles_and_adds_surcharge():
    assert baggage_fee("economy", 36, "international", False) == 2100


def test_infant_carry_on_limit():
    assert carry_on_ok(100, 2, True) is True
    assert carry_on_ok(100, 3, True) is False


def test_non_infant_weight_and_item_limits():
    assert carry_on_ok(7, 1, False) is True
    assert carry_on_ok(7.01, 1, False) is False
    assert carry_on_ok(5, 2, False) is False


@pytest.mark.parametrize("minutes,has_baggage,international,expected", [
    (60, True, False, "open"),
    (45, False, False, "open"),
    (120, True, True, "open"),
    (50, True, False, "late"),
    (110, True, True, "late"),
    (44, True, False, "closed"),
    (104, True, True, "closed"),
])
def test_check_in_status_examples(minutes, has_baggage, international, expected):
    assert check_in_status(minutes, has_baggage, international) == expected
