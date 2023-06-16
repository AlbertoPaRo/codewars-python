from counting_sheep import count_sheeps


def test_count_sheeps():
    input = [True,  True,  True,  False, True,  True,  True,  True, True,  False, True,
             False, True,  False, False, True, True,  True,  True,  True, False, False, True,  True]
    expected = 17
    assert count_sheeps(input) == expected
