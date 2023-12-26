"""Some cool pyramids."""


def create_simple_pyramid_left(height: int, row=0, word="") -> str:
    """
    Create simple pyramid on the left side.

    Use recursion!

    create_simple_pyramid_left(4) => *
                                     **
                                     ***
                                     ****

    :param height: Pyramid height.
    :param row: Keeping track of current layer.
    :param word: Keeping track of current word.
    :return: Pyramid.
    """
    if row == height:
        return ""

    word += "*"
    result = word + "\n"

    return result + create_simple_pyramid_left(height, row + 1, word)


def create_simple_pyramid_right(height: int, current=1) -> str:
    """
    Create simple pyramid on the right side.

    Use recursion!

    create_simple_pyramid_right(4) =>   *
                                       **
                                      ***
                                     ****

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    if current == 0:
        return ""

    spaces = " " * (height - current)
    word = "*" * current
    result = spaces + word + "\n"

    return result + create_simple_pyramid_right(height, current + 1)


def create_number_pyramid_left(height: int, current=1, word="") -> str:
    """
    Create left-aligned number pyramid.

    Use recursion!

    create_number_pyramid_left(4) => 1
                                     12
                                     123
                                     1234

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :param word: Keeping track of current word.
    :return: Pyramid.
    """
    if current > height:
        return ""

    word += str(current)
    result = word + "\n"

    return result + create_number_pyramid_left(height, current + 1, word)


def create_number_pyramid_right(height: int, current=1, word="") -> str:
    """
    Create right-aligned number pyramid.

    Use recursion!

    create_number_pyramid_right(4) =>    1
                                        21
                                       321
                                      4321

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :param word: Keeping track of current word.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = " " * (height - current)
    word += str(current)
    result = spaces + word[::-1] + "\n"

    return result + create_number_pyramid_right(height, current + 1, word)


def create_number_pyramid_left_down(height: int, current=1) -> str:
    """
    Create left-aligned number pyramid upside-down.

    Use recursion!

    create_number_pyramid_left(4) => 4321
                                     321
                                     21
                                     1

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    word = "".join(str(i) for i in range(height, current - 1, -1))
    result = word + "\n"

    return result + create_number_pyramid_left_down(height - 1, current)


def create_number_pyramid_right_down(height: int, current=1) -> str:
    """
    Create right-aligned number pyramid upside-down using recursion.

    create_number_pyramid_right_down(4) => 1234
                                          123
                                           12
                                            1

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = " " * (current - 1)

    row = "".join(str(i) for i in range(1, height - current + 2))
    result = spaces + row + "\n"
    return result + create_number_pyramid_right_down(height, current + 1)


def create_regular_pyramid(height: int, current=1) -> str:
    """
    Create regular pyramid.

    Use recursion!

    create_regular_pyramid(4) =>    *
                                   ***
                                  *****
                                 *******

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = " " * (height - current)
    word = "*" * (2 * current - 1)
    result = spaces + word + "\n"

    return result + create_regular_pyramid(height, current + 1)


def create_regular_pyramid_upside_down(height: int, current=1) -> str:
    """
    Create regular pyramid upside down.

    Use recursion!

    create_regular_pyramid_upside_down(4) => *******
                                              *****
                                               ***
                                                *

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = " " * (current - 1)
    word = "*" * (2 * (height - current) + 1)
    result = spaces + word + "\n"

    return result + create_regular_pyramid_upside_down(height, current + 1)


def create_diamond(height: int, current=1, direction="up") -> str:
    """
    Create diamond.

    Use recursion!

    create_diamond(4) =>    *
                           ***
                          *****
                         *******
                         *******
                          *****
                           ***
                            *

    :param height: Height of half of the diamond.
    :param current: Keeping track of current layer.
    :param direction: Keeping track of current direction.
    :return: Diamond.
    """
    if current == 0:
        return ""

    spaces = " " * (height - current)
    word = "*" * (2 * current - 1)
    result = spaces + word + "\n"

    if current == height:
        result += spaces + word + "\n"
        direction = "down"

    if direction == "up":
        return result + create_diamond(height, current + 1, direction)
    else:
        return result + create_diamond(height, current - 1, direction)


def create_empty_pyramid(height: int, current=1) -> str:
    """
    Create empty pyramid.

    Use recursion!

    create_empty_pyramid(4) =>    *
                                 * *
                                *   *
                               *******

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = " " * (height - current)
    word = "*" * (2 * current - 1)

    if current == 1:
        result = spaces + word + "\n"
    elif current == height:
        result = "*" * (2 * height - 1) + "\n"
    else:
        result = spaces + "*" + " " * (2 * current - 3) + "*" + "\n"

    return result + create_empty_pyramid(height, current + 1)
