"""Phone inventory."""


def phone_brand_and_models(all_phones: str):
    """
    Create a list of structured information about brands and models.

    For each different phone brand in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the brand (string),
    the second element is a list of models for the given brand (list of strings).

    No duplicate brands or models should be in the output.

    The order of the brands and models should be the same as in the input list (first appearance).

    "Honor Magic5,IPhone 11,IPhone 12,Google Pixel,Samsung Galaxy S22,IPhone 13,IPhone 13,Google Pixel2" =>
    [['Honor', ['Magic5']], ['IPhone', ['11', '12', '13']], ['Google', ['Pixel', 'Pixel2']], ['Samsung', ['Galaxy S22']]]
    """
    if all_phones:
        phone_list = all_phones.split(",")
        brand_model_list = []

        for phone in phone_list:
            brand, model = phone.split(" ", 1)
            found = False

            for entry in brand_model_list:
                if entry[0] == brand:
                    if model not in entry[1]:
                        entry[1].append(model)
                    found = True
                    break

            if not found:
                brand_model_list.append([brand, [model]])

        return brand_model_list

    return []


def add_phones(phone_list, all_phones) -> list:
    """
    Add phones from the list into the existing phone list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated phones (as in all the previous functions).
    The task is to add phones from the string into the list.

    Hint: This and phone_brand_and_models are very similar functions. Try to use one inside another.

    [['IPhone', ['11']], ['Google', ['Pixel']]] and "IPhone 12,Samsung Galaxy S22,IPhone 11"

        =>

    [['IPhone', ['11', '12']], ['Google', ['Pixel']], ['Samsung', ['Galaxy S22']]]
    """
    if all_phones:
        phones = all_phones.split(",")

        for phone in phones:
            brand, model = phone.split(" ", 1)
            found = False

            for entry in phone_list:
                if entry[0] == brand:
                    if model not in entry[1]:
                        entry[1].append(model)
                    found = True
                    break

            if not found:
                phone_list.append([brand, [model]])

    return phone_list


def number_of_phones(all_phones: str) -> list:
    """
    Create a list of tuples with brand quantities.

    The result is a list of tuples.
    Each tuple is in the form: (brand_name: str, quantity: int).
    The order of the tuples (brands) is the same as the first appearance in the list.

    "IPhone 12,Samsung Galaxy S22,IPhone 11"
    """
    if all_phones:
        phones = all_phones.split(",")
        counted_phones = {}

        for phone in phones:
            brand_name = phone.split()[0]

            if brand_name in counted_phones:
                counted_phones[brand_name] += 1
            else:
                counted_phones[brand_name] = 1

        return list(counted_phones.items())

    return []


def phone_list_as_string(phone_list: list) -> str:
    """
    Create a list of phones.

    The input list is in the same format as the result of phone_brand_and_models function.
    The order of the elements in the string is the same as in the list.
    [['IPhone', ['11']], ['Google', ['Pixel']]] =>
    "IPhone 11,Google Pixel"
    """
    phone_strings = []

    for brand, models in phone_list:
        brand_models = [f"{brand} {model}" for model in models]
        phone_strings.extend(brand_models)

    return ",".join(phone_strings)
