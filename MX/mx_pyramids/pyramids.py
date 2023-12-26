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
    print(word)

    return create_simple_pyramid_left(height, row + 1, word)


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

    spaces = " " * (height - current)
    word = "*" * current
    print(spaces + word)

    return create_simple_pyramid_right(height, current + 1)


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
    print(word)

    return create_number_pyramid_left(height, current + 1, word)


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
    print(spaces + word[::-1])

    return create_number_pyramid_right(height, current + 1, word)


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
    print(word)

    return create_number_pyramid_left_down(height - 1, current)


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

    row = "".join(str(i) for i in range(1, height - current + 2))
    print(row.rjust(height))

    return create_number_pyramid_right_down(height, current + 1)


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

    print(spaces + word)

    return create_regular_pyramid(height, current + 1)


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

    print(spaces + word)

    return create_regular_pyramid_upside_down(height, current + 1)


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

    if current == height:
        print(spaces + word)
        direction = "down"

    print(spaces + word)

    if direction == "up":
        return create_diamond(height, current + 1, direction)
    else:
        return create_diamond(height, current - 1, direction)


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
        print(spaces + word)
    elif current == height:
        print("*" * (2 * height - 1))
    else:
        print(spaces + "*" + " " * (2 * current - 3) + "*")

    return create_empty_pyramid(height, current + 1)
