from main_number_reversed_array import digitize


def test_digitize():
    input = 35231
    expected = [1, 3, 2, 5, 3]
    assert digitize(input) == expected
