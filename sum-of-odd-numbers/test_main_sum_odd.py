from main_sum_odd import row_sum_odd_numbers


def test_sum_odd():
    input = 13
    expected = 2197
    assert row_sum_odd_numbers(input) == expected
