def find_position_where_downstairs_entered(paren_str) -> int:
    """
    Finds the position in the string where Santa first goes downstairs

    Args:
        paren_str (str): string of parenthesis to check

    Returns:
        int: position where downstairs is first reached
    """
    floor_change_list = iter(1 if char == "(" else -1 for char in paren_str)
    sum_ = 0

    for position, val in enumerate(floor_change_list, start=1):
        sum_ += val
        if sum_ < 0:
            return position


def find_floor_santa_ends_on(paren_str) -> int:
    """
    _summary_

    Args:
        paren_str (_type_): _description_

    Returns:
        int: _description_
    """
    return paren_str.count("(") - paren_str.count(")")
