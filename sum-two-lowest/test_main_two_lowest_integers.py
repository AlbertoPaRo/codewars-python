from main_two_lowest_integers import sum_two_smallest_numbers


def test_sum_two_smallest_numbers():
    input = [5, 8, 12, 18, 22]
    expected = 13
    assert sum_two_smallest_numbers(input) == expected
