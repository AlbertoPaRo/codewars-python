from main_grade_book import get_grade


def test_get_grade():
    input = 95, 90, 93
    expected = "A"
    assert get_grade(*input) == expected
