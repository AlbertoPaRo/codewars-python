from main_string_to_array import string_to_array


def test_string_to_array():
    input = "Robin Singh"
    expected = ["Robin", "Singh"]
    assert string_to_array(input) == expected
