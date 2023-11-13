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
    assert students_study(12, True) is True
    assert students_study(17, True) is True


def test_students_study_during_day_without_coffee():
    """
    Test students studying at noon without coffee.

    Expected result: False.
    """
    assert students_study(5, False) is False
    assert students_study(12, False) is False
    assert students_study(17, False) is False


def test_students_study_during_evening_with_coffee():
    """
    Test students studying in the evening with coffee.

    Expected result: True.
    """
    assert students_study(18, True) is True
    assert students_study(20, True) is True
    assert students_study(23, True) is True


def test_students_study_during_evening_without_coffee():
    """
    Test students studying in the evening without coffee.

    Expected result: True.
    """
    assert students_study(18, False) is True
    assert students_study(21, False) is True
    assert students_study(23, False) is True


def test_students_study_during_night_with_coffee():
    """
    Test students studying at night with coffee.

    Expected result: False.
    """
    assert students_study(1, True) is False
    assert students_study(4, True) is False


def test_students_study_during_night_without_coffee():
    """
    Test students studying at night without coffee.

    Expected result: False.
    """
    assert students_study(1, False) is False
    assert students_study(4, False) is False


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
    assert lottery(-2, -2, -2) == 5
    assert lottery(0, 0, 0) == 5


def test_lottery_a_not_b_or_c():
    """
    Test when a is different from b and c.

    Expected result: 1.
    """
    assert lottery(1, 2, 2) == 1


def test_lottery_all_different():
    """
    Test when all numbers are different.

    Expected result: 1.
    """
    assert lottery(1, 2, 3) == 1


def test_lottery_a_same_as_b_or_c():
    """
    Test when a is same as b or c.

    Expected result: 0.
    """
    assert lottery(1, 1, 2) == 0
    assert lottery(2, 1, 2) == 0


def test_fruit_order_its_possible():
    """
    Test when it's possible to finish the order.

    Expected result: number of small fruit baskets.
    """
    assert fruit_order(0, 5, 25) == 0
    assert fruit_order(10, 0, 10) == 10
    assert fruit_order(5, 0, 5) == 5
    assert fruit_order(6, 0, 5) == 5
    assert fruit_order(10, 2, 20) == 10
    assert fruit_order(5, 5, 25) == 0
    assert fruit_order(3, 5, 13) == 3
    assert fruit_order(4, 5, 23) == 3
    assert fruit_order(5, 5, 30) == 5
    assert fruit_order(0, 100, 500) == 0
    assert fruit_order(300, 100, 800) == 300


def test_fruit_order_its_impossible():
    """
    Test when it's impossible to finish the order.

    Expected result: -1.
    """
    assert fruit_order(0, 5, 24) == -1
    assert fruit_order(0, 5, 21) == -1
    assert fruit_order(0, 5, 31) == -1
    assert fruit_order(0, 2, 15) == -1
    assert fruit_order(0, 3, 14) == -1
    assert fruit_order(3, 0, 10) == -1
    assert fruit_order(2, 0, 5) == -1
    assert fruit_order(5, 0, 20) == -1
    assert fruit_order(6, 0, 7) == -1
    assert fruit_order(6, 1, 12) == -1
    assert fruit_order(1, 1, 7) == -1
    assert fruit_order(47, 100, 548) == -1


def test_fruit_order_contains_zero():
    """
    Test when one or more numbers are zero.

    Expected result: 0.
    """
    assert fruit_order(0, 0, 0) == 0
    assert fruit_order(0, 1, 0) == 0
    assert fruit_order(1, 0, 0) == 0
    assert fruit_order(1, 1, 0) == 0
