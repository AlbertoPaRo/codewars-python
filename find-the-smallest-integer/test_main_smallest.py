from main_smallest import find_smallest_int


def test_smallest():
    input = 78, 56, 232, 12, 11, 43
    expected = 11
    assert find_smallest_int(input) == expected
