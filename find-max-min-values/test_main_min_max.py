from main_min_max import maximum,minimum

def test_maximum():
    input = [4,6,2,1,9,63,-134,566]
    expected = 566
    assert maximum(input) == expected
    
def test_minimum():
    input = [4,6,2,1,9,63,-134,566]
    expected = -134
    assert minimum(input) == expected

def test_min_unvars():
    input = [1, 2, 3, 4, 5, 10]
    expected = 1
    assert minimum(input) == expected