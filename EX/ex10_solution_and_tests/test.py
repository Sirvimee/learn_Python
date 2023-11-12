"""Test cases for solution."""

from solution import students_study
from solution import lottery
from solution import fruit_order


def test_students_study_during_day_with_coffee():
    """
    Test students studying at noon with coffee.

    Expected result: True.
    """
    assert students_study(5, True) is True


def test_students_study_during_day_without_coffee():
    """
    Test students studying at noon without coffee.

    Expected result: False.
    """
    assert students_study(5, False) is False


def test_students_study_during_evening_with_coffee():
    """
    Test students studying in the evening with coffee.

    Expected result: True.
    """
    assert students_study(18, True) is True


def test_students_study_during_evening_without_coffee():
    """
    Test students studying in the evening without coffee.

    Expected result: True.
    """
    assert students_study(18, False) is True


def test_students_study_during_night_with_coffee():
    """
    Test students studying at night with coffee.

    Expected result: False.
    """
    assert students_study(1, True) is False


def test_students_study_during_night_without_coffee():
    """
    Test students studying at night without coffee.

    Expected result: False.
    """
    assert students_study(1, False) is False


def test_lottery_all_numbers_fives():
    """
    Test when all numbers are fives.

    Expected result: 10.
    """
    assert lottery(5, 5, 5) == 10


def test_lottery_all_numbers_same_not_fives():
    """
    Test when all numbers are same but not fives.

    Expected result: 5.
    """
    assert lottery(1, 1, 1) == 5


def test_lottery_a_not_b_or_c():
    """
    Test when a is different from b and c.

    Expected result: 1.
    """
    assert lottery(1, 2, 2) == 1


def test_lottery_a_same_as_b_or_c():
    """
    Test when a is same as b or c.

    Expected result: 0.
    """
    assert lottery(1, 1, 2) == 0


def test_fruit_order_its_possible():
    """
    Test when it's possible to finish the order.

    Expected result: number of small fruit baskets.
    """
    assert fruit_order(4, 1, 9) == 4


def test_fruit_order_negative_numbers():
    """
    Test when one or more negative numbers.

    Expected result: -1.
    """
    assert fruit_order(-4, 1, 9) == -1


def test_fruit_order_its_impossible():
    """
    Test when it's impossible to finish the order.

    Expected result: -1.
    """
    assert fruit_order(4, 1, 10) == -1
