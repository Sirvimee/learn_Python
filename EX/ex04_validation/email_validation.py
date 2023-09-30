"""Email validation."""


def has_at_symbol(email: str):
    """
    Check if the email contains character "@".

    :param email: Email to be checked
    :return: True if the email contains "@", False otherwise
    """
    if "@" in email:
        return True
    return False


def is_valid_username(email: str):
    """
    Check if the email contains the valid username.

    Username is a part of the email address (the part before the @ symbol).
    Username cannot contain special characters (eg ?+-.,;:%¤#"&/).
    The only allowed special character is dot(.).

    :param email: Email to be checked
    :return: True if the username part of the given email address passes validation, False otherwise
    """
    at_counter = email.count("@")

    if at_counter > 1:
        return False

    username = email.split("@")[0]

    for letter in username:
        if not letter.isalnum():
            if letter != ".":
                return False
    return True


def find_domain(email: str):
    """
    Find domain from email.

    :param email: Email to be checked
    :return: Domain
    """
    domain = email.split("@")[-1]

    return domain


def is_valid_domain(email: str):
    """
    Check if the domain is valid.

    Valid domain contains one dot ("."),
    contains only letters in addition to the dot.
    There can be 3-10 characters between the @-symbol and the dot.
    There can be 2-5 characters after the dot.

    :param email: Email to be checked
    :return: True if the email address passes validation, False otherwise
    """
    domain = find_domain(email)

    if domain.count(".") == 1:
        if all(letter.isalpha() or letter == "." for letter in domain):
            if 3 <= len(domain.split(".")[0]) <= 10:
                if 2 <= len(domain.split(".")[1]) <= 5:
                    return True
    return False


def is_valid_email_address(email: str):
    """
    Check whether the given email is valid.

    Valid email contains character "@", valid username and valid domain.

    :param email: Email to be checked
    :return: True if the email is valid, False otherwise.
    """

    return (
        has_at_symbol(email) and
        is_valid_username(email) and
        is_valid_domain(email)
    )


def create_email_address(domain: str, username: str):
    """
    Create email address from given username and domain.

    The created email must be correct and pass validations.

    :param domain: Domain provided
    :param username: Username provided
    :return: If it is possible to create a correct email address with the given arguments,
    the function returns this address, if not, the function returns:
    "Cannot create a valid email address using the given parameters!"
    """
    email = username + "@" + domain

    if is_valid_email_address(email):
        return email
    return "Cannot create a valid email address using the given parameters!"


if __name__ == '__main__':
    print("Email has the @ symbol:")
    print(has_at_symbol("joonas.kivi@gmail.com"))  # -> True
    print(has_at_symbol("joonas.kivigmail.com"))  # -> False

    print("\nUsername has no special symbols:")
    print(is_valid_username("martalumi@taltech.ee"))  # -> True
    print(is_valid_username("marta.lumi@taltech.ee"))  # -> True
    print(is_valid_username("marta lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta&lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta@lumi@taltech.ee"))  # -> False

    print("\nFind the email domain name:")
    print(find_domain("karla.karu@saku.ee"))  # -> saku.ee
    print(find_domain("karla.karu@taltech.ee"))  # -> taltech.ee
    print(find_domain("karla.karu@yahoo.com"))  # -> yahoo.com
    print(find_domain("karla@karu@yahoo.com"))  # -> yahoo.com

    print("\nCheck if the domain is correct:")
    print(is_valid_domain("pihkva.pihvid@ttu.ee"))  # -> True
    print(is_valid_domain("metsatoll@&gmail.com"))  # -> False
    print(is_valid_domain("ewewewew@i.u.i.u.ewww"))  # -> False
    print(is_valid_domain("pannkook@m.oos"))  # -> False

    print("\nIs the email valid:")
    print(is_valid_email_address("DARJA.darja@gmail.com"))  # -> True
    print(is_valid_email_address("DARJA=darjamail.com"))  # -> False

    print("\nCreate your own email address:")
    print(create_email_address("hot.ee", "vana.ema"))  # -> vana.ema@hot.ee
    print(create_email_address("jaani.org", "lennakuurma"))  # -> lennakuurma@jaani.org
    print(create_email_address("koobas.com",
                               "karu&pojad"))  # -> Cannot create a valid email address using the given parameters!

