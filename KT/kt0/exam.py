"""KT0."""


def add_char_into_pos(char: str, pos: int, string: str) -> str:
    """
    Return a string where a given character is added into a given position in a string.

    In the case of empty string and position 1, return the given character.

    add_char_into_pos("a", 2, "kheksa") -> "kaheksa"
    add_char_into_pos("t", 8, "kaheksa") -> "kaheksat"
    add_char_into_pos("a", 1, "mps") -> "amps"
    add_char_into_pos("a", 1, "") -> "a"
    add_char_into_pos("k", 10, "kalla") -> "kalla"

    """
    if pos == len(string) + 1:
        return string + char

    if pos > len(string) + 1:
        return string

    return string[:pos - 1] + char + string[pos - 1:]


def nr_of_common_characters(string1: str, string2: str) -> int:
    """
    Return a number of common characters of string1 and string2.

    Do not take into account repeated characters.

    common_characters("iva", "avis") -> 3 # 'a', 'i', 'v' are common
    common_characters("saali", "pall") -> 2  # 'a', 'l' are common
    common_characters("memm", "taat") -> 0
    common_characters("memm", "") -> 0

    """
    common_chars = []

    for char1 in string1:
        for char2 in string2:
            if char1 == char2:
                if char1 not in common_chars:
                    common_chars.append(char1)

    return len(common_chars)
    # teine lahendus
    # return len(set(string1).intersection(set(string2)))


def nr_into_num_list(nr: int, num_list: list) -> list:
    """
    Return a list of numbers where the "nr" is added into the "num_list" so that the list keep going to be sorted.

    Built-in sort methods are not allowed.

    nr_into_num_list(5, []) -> [5]
    nr_into_num_list(5, [1,2,3,4]) -> [1,2,3,4,5]
    nr_into_num_list(5, [1,2,3,4,5,6]) -> [1,2,3,4,5,5,6]
    nr_into_num_list(0, [1,2,3,4,5]) -> [0,1,2,3,4,5,]

    """
    if not num_list:
        return [nr]

    index = 0
    for i in range(len(num_list)):
        if num_list[i] <= nr:
            index = i + 1
        else:
            break

    return num_list[:index] + [nr] + num_list[index:]


def symbol_average_position_in_words(words: list) -> dict:
    """
    Find the average position for each symbol.

    For the given text (list of words) the function has to find
    the average position for each symbol.

    If the list is: ["hello", "world"]
    then the positions for the symbols are:
    h: 0 (in the first word only)
    e: 1
    l: 2, 3, 3 (2, 3 in the first word, 3 in the second)
    o: 4, 1
    w: 0
    r: 2
    d: 4

    The average positions:
    h: 0
    e: 1
    l: 2.67
    o: 2.5
    w: 0
    r: 2
    d: 4
    Positions should be rounded to 2 places after the decimal point.

    The order of the keys in the dictionary is not important.

    symbol_average_position_in_words(["hello", "world"]) =>
    {'h': 0.0, 'e': 1.0, 'l': 2.67, 'o': 2.5, 'w': 0.0, 'r': 2.0, 'd': 4.0}

    symbol_average_position_in_words(["abc", "a", "bc", ""]) =>
    {'a': 0.0, 'b': 0.5, 'c': 1.5}

    symbol_average_position_in_words(["1", "a", "A"]) =>
    {'1': 0.0, 'a': 0.0, 'A': 0.0}

    :param words: list of words
    :return: dictionary with symbol average positions
    """
    positions_dict = {}
    final_dict = {}

    for word in words:
        for i in range(len(word)):
            char = word[i]
            if char not in positions_dict:
                positions_dict[char] = [i]
            else:
                positions_dict[char].append(i)

    for key, value in positions_dict.items():
        if len(value) == 1:
            final_dict[key] = float(round(value[0], 2))
        else:
            total_position = sum(value)
            final_dict[key] = float(round(total_position / len(value), 2))

    return final_dict


def str_dist(string: str, sub: str) -> int:
    """
    Return the length of the largest substring which starts and ends with sub.

    Given a string and a non-empty substring sub,
    compute recursively the largest substring which starts and ends with sub and return its length.

    str_dist("catcowcat", "cat") => 9
    str_dist("catcowcat", "cow") => 3
    str_dist("cccatcowcatxx", "cat") => 9
    """
    if string == "" or sub == "":
        return 0

    if string[:len(sub)] == sub and string[-len(sub):] == sub:
        return len(string)

    if string[:len(sub)] != sub:
        return str_dist(string[1:], sub)

    if string[-len(sub):] != sub:
        return str_dist(string[:-1], sub)

    return str_dist(string[1:-1], sub)

    # teine lahendus
    # if string == "" or sub == "":
    #     return 0
    # if string.startswith(sub) and string.endswith(sub):
    #     return len(string)
    # if not string.startswith(sub):
    #     return str_dist(string[1:], sub)
    # else:
    #     return str_dist(string[:-1], sub)
