from solution.src.santa_floor_functions import find_floor_santa_ends_on


def test_floors_resulting_in_zero():
    """
    tests that given floors end in zero
    """
    paren_str = "(())"
    assert find_floor_santa_ends_on(paren_str) == 0

    paren_str = "()()"
    assert find_floor_santa_ends_on(paren_str) == 0


def test_floors_resulting_in_three():
    """
    tests that given floors end in three
    """
    paren_str = "((("
    assert find_floor_santa_ends_on(paren_str) == 3

    paren_str = "(()(()("
    assert find_floor_santa_ends_on(paren_str) == 3

    paren_str = "))((((("
    assert find_floor_santa_ends_on(paren_str) == 3


def test_floors_rseulting_in_negative():
    """
    tests that function correctly outputs negative values for coreesponding
    floors
    """
    paren_str = "())"
    assert find_floor_santa_ends_on(paren_str) == -1

    paren_str = "))("
    assert find_floor_santa_ends_on(paren_str) == -1

    paren_str = ")))"
    assert find_floor_santa_ends_on(paren_str) == -3

    paren_str = ")())())"
    assert find_floor_santa_ends_on(paren_str) == -3
