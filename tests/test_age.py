from age import get_age
import pytest


def test_get_age():
    # Given.
    yyyy = 1939
    mm = 12
    dd = 11
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 83
