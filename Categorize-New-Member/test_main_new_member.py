from main_new_member import open_or_senior


def test_open_or_senior():
    input = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
    expected = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
    assert open_or_senior(input) == expected
