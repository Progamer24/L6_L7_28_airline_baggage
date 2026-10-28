"""Branch coverage tests for airline_baggage.py.

Run from this directory with:
    python -m coverage run --branch --source=airline_baggage -m pytest -q BranchCoverageTest_airline_baggage.py
    python -m coverage report -m
"""
import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


@pytest.mark.parametrize("cabin", ["economy", "premium", "business"])
def test_known_cabins(cabin):
    assert baggage_fee(cabin, 0, "domestic", False) == 0


def test_unknown_cabin_branch():
    with pytest.raises(ValueError):
        baggage_fee("unknown", 1, "domestic", False)


@pytest.mark.parametrize("weight", [-1, -0.01])
def test_negative_weight_branch(weight):
    with pytest.raises(ValueError):
        baggage_fee("economy", weight, "domestic", False)


def test_zero_and_positive_weight():
    assert baggage_fee("economy", 0, "domestic", False) == 0
    assert baggage_fee("economy", 16, "domestic", False) == 20


@pytest.mark.parametrize("cabin,weight,member,expected", [
    ("economy", 25, True, 0),       # member allowance branch
    ("economy", 16, False, 20),     # non-member branch
    ("business", 41, True, 20),     # business member exclusion
])
def test_membership_and_allowance_branches(cabin, weight, member, expected):
    assert baggage_fee(cabin, weight, "domestic", member) == expected


def test_excess_boundary_and_route_branches():
    assert baggage_fee("economy", 15, "domestic", False) == 0
    assert baggage_fee("economy", 16, "domestic", False) == 20
    assert baggage_fee("economy", 16, "international", False) == 45


def test_large_excess_branches():
    # Exactly 20 kg excess does not enter the >20 branch.
    assert baggage_fee("economy", 35, "domestic", False) == 400
    assert baggage_fee("economy", 36, "domestic", False) == 840
    assert baggage_fee("economy", 36, "international", False) == 2100


def test_infant_true_and_false_branches():
    assert carry_on_ok(50, 2, True) is True
    assert carry_on_ok(50, 3, True) is False
    assert carry_on_ok(5, 1, False) is True


def test_non_infant_weight_branches():
    assert carry_on_ok(7, 1, False) is True
    assert carry_on_ok(7.01, 1, False) is False


def test_non_infant_item_branches():
    assert carry_on_ok(5, 1, False) is True
    assert carry_on_ok(5, 2, False) is False


@pytest.mark.parametrize("minutes,has_baggage,international,expected", [
    (60, True, False, "open"),     # cutoff boundary
    (59, True, False, "late"),
    (44, True, False, "closed"),
    (45, False, False, "open"),
    (30, False, False, "late"),
    (29, False, False, "closed"),
    (120, False, True, "open"),
    (100, False, True, "late"),
    (89, False, True, "closed"),
])
def test_check_in_cutoff_branches(minutes, has_baggage, international, expected):
    assert check_in_status(minutes, has_baggage, international) == expected
