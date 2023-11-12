"""Test cases for solution."""

from solution import *


def test_students_study_during_day_with_coffee():
    """
    The one with the coffee at noon.

    During the day, students study when there is coffee.
    This case represents the time period of a day and coffee is present.
    Expected result: True.
    """
    assert students_study(12, True) is True
    assert students_study(5, True) is True
    assert students_study(17, True) is True


def test_students_study_during_day_without_coffee():
    """
    The one without the coffee at noon.

    During the day, students study when there is coffee.
    This case represents the time period of a day and coffee is not present.
    Expected result: False.
    """
    assert students_study(12, False) is False
    assert students_study(5, False) is False
    assert students_study(17, False) is False


def test_students_study_during_evening_with_coffee():
    """
    The one with the coffee at evening.

    During the evening, students study when there is no coffee.
    This case represents the time period of a evening and coffee is present.
    Expected result: False.
    """
    assert students_study(20, True) is False
    assert students_study(18, True) is False
    assert students_study(24, True) is False


def test_students_study_during_evening_without_coffee():
    """
    The one without the coffee at evening.

    During the evening, students study when there is no coffee.
    This case represents the time period of a evening and coffee is not present.
    Expected result: True.
    """
    assert students_study(20, False) is True
    assert students_study(18, False) is True
    assert students_study(24, False) is True


def test_students_study_during_night_with_coffee():
    """
    The one with the coffee at night.

    During the night, students sleep.
    This case represents the time period of a night and coffee is present.
    Expected result: False.
    """
    assert students_study(1, True) is False
    assert students_study(3, True) is False
    assert students_study(4, True) is False


def test_students_study_during_night_without_coffee():
    """
    The one without the coffee at night.

    During the night, students sleep.
    This case represents the time period of a night and coffee is not present.
    Expected result: False.
    """
    assert students_study(1, False) is False
    assert students_study(3, False) is False
    assert students_study(4, False) is False


def test_lottery_all_numbers_fives():
    """
    The one with all numbers five.
    Expected result: 10.
    """
    assert lottery(5, 5, 5) == 10


def test_lottery_all_numbers_same_not_fives():
    """
    The one with all numbers are same but not fives.
    Expected result: 5.
    """
    assert lottery(1, 1, 1) == 5
    assert lottery(3, 3, 3) == 5
    assert lottery(0, 0, 0) == 5
    assert lottery(10, 10, 10) == 5
    assert lottery(-5, -5, -5) == 5


def test_lottery_a_not_b_or_c():
    """
    The one with both b and c are different from a.
    Expected result: 1.
    """
    assert lottery(1, 2, 2) == 1
    assert lottery(3, 4, 5) == 1
    assert lottery(0, 1, 3) == 1
    assert lottery(1, -1, 3) == 1


def test_lottery_a_same_as_b_or_c():
    """
    The one with a is same as b or c.
    Expected result: 0.
    """
    assert lottery(1, 1, 2) == 0
    assert lottery(3, 4, 3) == 0
    assert lottery(-3, 4, -3) == 0


def test_fruit_order_its_possible():
    """
    The one where it's possible to finish the order.
    Expected result: number of small fruit baskets.
    """
    assert fruit_order(4, 1, 9) == 4
    assert fruit_order(4, 2, 14) == 4
    assert fruit_order(1, 2, 11) == 1
    assert fruit_order(0, 1, 5) == 0


def test_fruit_order_negative_numbers():
    """
    The one with one or more negative numbers.
    Expected result: -1.
    """
    assert fruit_order(-4, 1, 9) == -1
    assert fruit_order(4, -2, 14) == -1
    assert fruit_order(1, 2, -11) == -1


def test_fruit_order_its_impossible():
    """
    The one where it's impossible to finish the order.
    Expected result: -1.
    """
    assert fruit_order(4, 1, 10) == -1
    assert fruit_order(4, 1, 14) == -1
    assert fruit_order(2, 2, 11) == -1
    assert fruit_order(0, 0, 5) == -1
