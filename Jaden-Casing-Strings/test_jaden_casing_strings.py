from jaden_casing_strings import to_jaden_case


def test_to_jaden_case():
    input = "How can mirrors be real if our eyes aren't real"
    expected = "How Can Mirrors Be Real If Our Eyes Aren't Real"
    assert to_jaden_case(input) == expected
