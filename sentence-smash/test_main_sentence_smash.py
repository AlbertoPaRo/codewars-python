from main_sentence_smash import smash


def test_smash():
    input = ["hello", "world"]
    expected = "hello world"
    assert smash(input) == expected
