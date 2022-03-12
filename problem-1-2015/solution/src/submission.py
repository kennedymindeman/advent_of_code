from os import environ

from aocd import get_data, submit

from src.santa_floor_functions import (
    find_floor_santa_ends_on,
    find_position_where_downstairs_entered,
)

kwargs = {"day": 1, "year": 2015, "session": environ["SESSION"]}
paren_str = get_data(**kwargs)

submit(find_floor_santa_ends_on(paren_str), **kwargs, part="a")
submit(find_position_where_downstairs_entered(paren_str), **kwargs, part="b")
