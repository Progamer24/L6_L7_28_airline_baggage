from hypothesis import given, strategies as st

from airline_baggage import parse_booking, tag_label, total_weight


@given(st.one_of(st.text(), st.none()))
def test_parse_booking_no_crash(value):
    result = parse_booking(value)
    assert isinstance(result, tuple)
    assert len(result) == 3


@given(st.one_of(st.text(), st.none()))
def test_total_weight_no_crash(value):
    result = total_weight(value)
    assert isinstance(result, float)
    assert result >= 0


@given(st.one_of(st.text(), st.none()))
def test_tag_label_no_crash(value):
    result = tag_label(value)
    assert isinstance(result, str)


def test_parse_booking_valid_code():
    assert parse_booking("AI-203-12A") == ("AI", 203, "A")


def test_invalid_booking_returns_empty_result():
    assert parse_booking("not-a-booking") == ("", 0, "")
    assert parse_booking(None) == ("", 0, "")


def test_total_weight_sums_valid_non_negative_values():
    assert total_weight("12.5, 7, 23") == 42.5
    assert total_weight("12.5, invalid, -2, 7") == 19.5
    assert total_weight("inf, nan, 3") == 3.0


def test_tag_label_valid_name():
    assert tag_label("Asha Sharma") == "A. SHARMA"


def test_invalid_name_returns_empty_label():
    assert tag_label("Asha") == ""
    assert tag_label(None) == ""
