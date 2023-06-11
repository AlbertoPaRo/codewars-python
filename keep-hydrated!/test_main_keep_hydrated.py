from main_keep_hydrated import litres


def test_keep_hydrated():
    input = 2
    expected = 1
    assert litres(input) == expected
