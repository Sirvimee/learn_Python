"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.

    :param letter: secret letter
    :return: validation
    """
    lowercase_chars = 0
    uppercase_chars = 0
    sum_of_digits = 0

    for char in letter:
        if char.islower():
            lowercase_chars += 1
        if char.isupper():
            uppercase_chars += 1

    if uppercase_chars > lowercase_chars:
        for char in letter:
            if char.isdigit():
                sum_of_digits += int(char)

    if sum_of_digits <= uppercase_chars:
        if sum_of_digits >= lowercase_chars:
            return True
        else:
            return False


if __name__ == '__main__':
    print(secret_letter("sOMEteSTLETTer8"))  # True
    print(secret_letter("thisisNOTvaliD4"))  # False
    print(secret_letter("TOOMANYnumbers99"))  # False
    print(secret_letter("anotherVALIDLETTER17"))  # True
    print(secret_letter("CANBENOLOWERCASENODIGITS"))  # True
