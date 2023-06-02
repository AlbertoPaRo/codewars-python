from main_sum_mixed_array import sum_mix


def test_sum_mix():
    input = [9, 3, '7', '3']
    expected = 22
    assert sum_mix(input) == expected
