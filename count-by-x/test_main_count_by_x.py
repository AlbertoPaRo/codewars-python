from main_count_by_x import count_by


def test_count_by():
    input = [1, 5]
    expected = [1, 2, 3, 4, 5]
    assert count_by(*input) == expected
