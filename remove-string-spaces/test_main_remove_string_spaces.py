from main_remove_string_spaces import no_space


def test_no_space():
    input = '8 j 8   mBliB8g  imjB8B8  jl  B'
    expected = '8j8mBliB8gimjB8B8jlB'
    assert no_space(input) == expected
