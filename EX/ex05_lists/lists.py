"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    """
    return all_phones.split(",")


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google", "Honor"]
    """
    list_of_phones = all_phones.split(",")
    list_of_brands = []

    for phone in list_of_phones:
        brand = phone.split(" ")
        if brand[0] not in list_of_brands:
            list_of_brands.append(brand[0])

    return list_of_brands


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).

    "Honor Magic5,Google Pixel,Honor Magic4" => ['Magic5', 'Pixel', 'Magic4']
    """
    list_of_phones = all_phones.split(",")
    list_of_models = []

    for phone in list_of_phones:
        model = phone.split(" ")
        model = " ".join(model[1:])
        if model[1:len(model)] not in list_of_models:
            list_of_models.append(model)

    return list_of_models


def search_by_brand(all_phones: str, search_brand: str) -> list:
    """
    Return list of phone models of the brand looking for.

    The function searches for exact matches, not a case sensitive.
    The result is the phones in their original form.
    """
    list_of_phones = all_phones.split(",")
    found_phones = []

    for phone in list_of_phones:
        if search_brand.lower() in phone.lower():
            found_phones.append(phone)

    return found_phones


def search_by_model(all_phones: str, search_model: str) -> list:
    """
    Return list of phone models of the models looking for.

    The function searches for exact matches models, not a case sensitive and returns models with brands.
    The result is the phones in their original form.
    """
    list_of_phones = all_phones.split(",")
    found_phones = []

    for phone in list_of_phones:
        sliced_phone = phone.split()
        sliced_phone.pop(0)
        for element in sliced_phone:
            if search_model.lower() == element.lower():
                found_phones.append(phone)

    return found_phones
