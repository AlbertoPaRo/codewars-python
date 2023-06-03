from main_third_angle import other_angle


def test_other_angle():
    input = 30, 60
    expected = 90
    assert other_angle(*input) == expected
