"""A small exercise in zookeeping."""
from functools import reduce
import math


def parse_animal(animal_str: str) -> list:
    """
    Parse a string containing animal data and return a structured list.

    The input string is expected to be in the format:
    "species,scientific_name,age_up_to,weight_range,height_range,diet,habitat"

    The returned list structure is as follows:
    [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    Example:
    Input:  "African bush elephant,Loxodonta africana,70,3000-6000,2.2-4,herbivorous,savannah"
    Output: ['African bush elephant', 'Loxodonta africana', 70, [3000.0, 6000.0], [2.2, 4.0], 'herbivorous', 'savannah']

    :param animal_str: The input string containing animal data.
    :return: A list containing structured animal data.
    """

    def convert_to_number(data):
        if '.' in data:
            return float(data)
        return int(data)

    species, scientific_name, age_up_to, weight_range, height_range, diet, habitat = animal_str.split(',')

    min_weight, max_weight = map(convert_to_number, weight_range.split('-'))
    min_height, max_height = map(convert_to_number, height_range.split('-'))

    return [species, scientific_name, int(age_up_to), [min_weight, max_weight], [min_height, max_height], diet, habitat]


def list_species_and_scientific_names(animal_data: list) -> list:
    """
    Extract and return species' common and scientific names from the given animal data.

    The function maps through the provided list and returns a list of tuples.
    Each tuple contains the common name (species name) as the first element
    and the scientific name as the second element.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: List of structured animal data.
    :return: List of tuples, where each tuple is structured as (common_name, scientific_name).
    """
    return list(map(lambda animal: (animal[0], animal[1]), animal_data))


def animals_starting_with(animal_data: list, letter: str) -> list:
    """
    Return a list of animals where the common name starts with the provided letter.

    For instance, if the letter is 'A', it would return animals like 'Aardvark' or 'Antelope'.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: A list containing details about multiple animals.
    :param letter: The starting letter to filter animals by.
    :return: An alphabetically sorted list of common names of animals that start with the given letter.
    """
    filtered_animals = list(filter(lambda animal: animal[0].startswith(letter), animal_data))
    return sorted(map(lambda animal: animal[0], filtered_animals))


def find_how_many_pumpkins_are_needed_to_feed_animals(animal_data: list) -> int:
    """
    Calculate the number of pumpkins required to feed all herbivorous and omnivorous animals over winter.

    Assumptions:
    1. There are 2 animals of each species.
    2. Each animal consumes an average of 6% of its body weight in pumpkins daily.
    3. A pumpkin weighs 3kg.
    4. Winter lasts 90 days.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: List of structured animal data.
    :return: Total number of pumpkins needed, rounded up to the nearest whole number.
    """
    def calculate_pumpkins_for_animal(animal):
        total_pumpkins = ((animal[3][0] + animal[3][1]) * 0.06 / 3) * 90
        return total_pumpkins

    herbivorous_and_omnivorous = list(filter(lambda animal: animal[5] in ['herbivorous', 'omnivorous'], animal_data))

    return math.ceil(reduce(lambda total, animal: total + calculate_pumpkins_for_animal(animal),
                            herbivorous_and_omnivorous, 0))


def total_noise_level(animal_data: list) -> float:
    """
    Calculate the total noise level based on the weight of all animals. There is just one animal of each species.

    The noise level for each animal is calculated as 0.01 times the average of their weight range.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: A list containing details about multiple animals.
    :return: The total noise level of all animals in the list.
    """
    return sum(map(lambda animal: (animal[3][0] + animal[3][1]) / 2 * 0.01, animal_data))


def zoo_parade_length(animal_data: list) -> float:
    """
    Calculate the total length of a zoo parade based on the horizontal length of all animals. There is just one animal of each species.

    The length added by each animal is assumed to be equivalent to the average of their height range.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: A list containing details about multiple animals.
    :return: The total parade length of all animals in the list.
    """
    return sum(map(lambda animal: animal[4][0] + animal[4][1], animal_data)) / 2


def animal_olympics_winner(animal_data: list) -> str:
    """
    Determine the winner of the Animal Olympics based on speed.

    The speed of an animal is inversely proportional to their weight; lighter animals are faster.
    The fastest animal is determined based on the average of their weight range.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: A list containing details about multiple animals.
    :return: The species name of the winning animal.
    """
    return min(animal_data, key=lambda animal: (animal[3][0] + animal[3][1]) / 2)[0]


def total_feather_count(animal_data: list) -> float:
    """
    Calculate the total feather count for all animals. There is just one animal of each species.

    The feather count for each animal is calculated as 1000 times the average of their weight range.
    (Note: This is a fictional metric for the sake of this exercise.)

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: A list containing details about multiple animals.
    :return: The total feather count of all animals in the list.
    """
    min_weight = sum(map(lambda animal: animal[3][0], animal_data))
    max_weight = sum(map(lambda animal: animal[3][1], animal_data))
    summa = min_weight + max_weight
    return round(summa / 2 * 1000, 1)


def zoo_weight_on_other_planet(animal_data: list) -> float:
    """
    Calculate the total weight of the zoo on another planet. There is just one animal of each species.

    The weight on the other planet is 50% of the Earth's weight for each animal.
    The weight used for each animal is the average of their weight range.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: A list containing details about multiple animals.
    :return: The total weight of the zoo on the other planet.
    """
    return sum(map(lambda animal: (animal[3][0] + animal[3][1]) / 2, animal_data)) / 2


def sort_alphabetically_by_scientific_name(animal_data: list) -> list:
    """
    Sort animals by scientific names.

    Sort animals by their scientific names in ascending alphabetical order and return a tuple of
    (common name, scientific name) for each animal.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: List of structured animal data.
    :return: List of tuples with (common name, scientific name) sorted by scientific name.
    """
    return sorted(tuple(list_species_and_scientific_names(animal_data)), key=lambda animal: (animal[1]))


def find_animals_whose_height_is_less_than(animal_data: list, height_limit: float) -> list:
    """
    Identify animals that do not exceed a specified height, considering the maximum possible height for each species.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: List of structured animal data.
    :param height_limit: Maximum height (in meters) as a float.
    :return: List of common names of animals that are shorter than the height limit, sorted from shortest to tallest.
    """
    filtered_animal = sorted(filter(lambda animal: animal[4][1] < height_limit, animal_data), key=lambda x: x[4][1])
    return list(map(lambda animal: animal[0], filtered_animal))


def filter_animals_based_on_diet(animal_data: list, diet: str) -> list:
    """
    Filter animals based on their dietary habits.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: List of structured animal data.
    :param diet: A string indicating the diet (e.g., "herbivorous", "carnivorous").
    :return: Alphabetically sorted list of common names of animals that match the specified diet.
    """
    filtered_animal = list(filter(lambda animal: animal[5] == diet, animal_data))
    return sorted(map(lambda animal: animal[0], filtered_animal))


def find_animal_with_longest_lifespan(animal_data: list) -> str:
    """
    Identify the animal with the longest potential lifespan.

    In the case of a tie, the function will return the name of the first occurrence.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: List of structured animal data.
    :return: The common name of the animal with the longest lifespan.
    """
    animal_with_longest_lifespan = max(animal_data, key=lambda animal: animal[2])
    return animal_with_longest_lifespan[0]


def create_animal_descriptions(animal_data: list) -> list:
    """
    Generate descriptions for each animal, suitable for display at the zoo.

    The description format is:
    "[Species name] ([Scientific name]) lives in [habitat] and its diet is [diet].
     These animals can live up to [max age] years, and they weigh between [min weight]
     kg and [max weight] kg as adults."

     Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: List of structured animal data.
    :return: List of string descriptions for each animal.
    """
    info = list(map(lambda animal: f"{animal[0]} ({animal[1]}) lives in {animal[6]} and its diet is {animal[5]}. "
                                   f"These animals can live up to {animal[2]} years, "
                                   f"and they weigh between {animal[3][0]} kg "
                                   f"and {animal[3][1]} kg as adults.", animal_data))
    return info


def calculate_ecological_impact_score(animal_data: list) -> float:
    """
    Calculate a combined ecological impact score for all animals in the zoo.

    The score is calculated based on factors such as the animal's average weight, diet, and habitat.
    Each animal starts with a base score of 10. Additional factors are applied as follows:

    - Weight Factor: Adds 0.001 times the average weight of the animal to the score.
    - Diet Factor: Multiplies the score by a factor based on the diet.
      - Herbivorous: 1.2
      - Carnivorous: 1.5
      - Omnivorous: 1.3
    - Habitat Factor: Adds a fixed score based on the habitat.
      - Savannah: +5
      - Tropics: +4
      - Temperate Forest: +3
    If the habitat is not one of the ones listed above, the habitat score is considered 0.

    The final score is the sum of individual scores of all animals.

    Reminder: [species, scientific_name, age_up_to, [min_weight, max_weight], [min_height, max_height], diet, habitat]

    :param animal_data: List of structured animal data.
    :return: The total ecological impact score.
    """
    def calculate_score_for_animal(animal):
        base_score = 10
        average_weight = (animal[3][0] + animal[3][1]) / 2

        weight_factor = 0.001 * average_weight
        diet_factor = {'herbivorous': 1.2, 'carnivorous': 1.5, 'omnivorous': 1.3}.get(animal[5], 1)
        habitat_factor = {'savannah': 5, 'tropics': 4, 'temperate forest': 3}.get(animal[6].lower(), 0)

        total_score = base_score + weight_factor
        total_score *= diet_factor
        total_score += habitat_factor

        return total_score

    return reduce(lambda total, animal: total + calculate_score_for_animal(animal), animal_data, 0)


if __name__ == '__main__':
    test_data = [
        "African bush elephant,Loxodonta africana,70,3000-6000,2.2-4,herbivorous,savannah",
        "Little red flying-fox,Pteropus scapulatus,30,0.3-0.6,0.24-0.26,herbivorous,tropics",
        "Giraffe,Giraffa camelopardalis,25,1200-1800,4.3-5.7,herbivorous,savannah",
        "Eurasian lynx,Lynx lynx,7,60-75,0.55-0.75,carnivorous,temperate forest",
        "Brown bear,Ursus arctos,33,130-217,1.4-2.8,omnivorous,temperate forest"
    ]
    animal_data = list(map(parse_animal, test_data))
    print(animal_data)

    print(list_species_and_scientific_names(animal_data))
    # Expected Output: [('African bush elephant', 'Loxodonta africana'),
    # ('Little red flying-fox', 'Pteropus scapulatus'),
    # ('Giraffe', 'Giraffa camelopardalis'), ('Eurasian lynx', 'Lynx lynx'), ('Brown bear', 'Ursus arctos')]

    print(animals_starting_with(animal_data, 'L'))
    # Expected Output: ["Little red flying-fox"]

    print("Pumpkins: " + str(find_how_many_pumpkins_are_needed_to_feed_animals(animal_data)))
    # Pumpkins: 22227

    print("Noise: " + str(total_noise_level(animal_data)))
    # Noise: 62.4145

    print("Parade: " + str(zoo_parade_length(animal_data)))
    # Parade: 11.1

    print("Olympics: " + animal_olympics_winner(animal_data))
    # Olympics: 'Little red flying-fox'

    print("Feathers: " + str(total_feather_count(animal_data)))
    # Feathers: 6241450.0

    print("Planet: " + str(zoo_weight_on_other_planet(animal_data)))
    # Planet: 3120.725

    print(sort_alphabetically_by_scientific_name(animal_data))
    # Expected Output: [('Giraffe', 'Giraffa camelopardalis'), ('African bush elephant', 'Loxodonta africana'),
    # ('Eurasian lynx', 'Lynx lynx'), ('Little red flying-fox', 'Pteropus scapulatus'), ('Brown bear', 'Ursus arctos')]

    print(find_animals_whose_height_is_less_than(animal_data, 2))
    # Expected Output: ['Little red flying-fox', 'Eurasian lynx']

    print(filter_animals_based_on_diet(animal_data, "herbivorous"))
    # Expected Output: ['African bush elephant', 'Giraffe', 'Little red flying-fox']

    print(find_animal_with_longest_lifespan(animal_data))
    # Expected Output: 'African bush elephant'

    print(create_animal_descriptions(animal_data))
    # Expected Output:
    # ["African bush elephant (Loxodonta africana) lives in savannah and its diet is herbivorous.
    # These animals can live up to 70 years, and they weigh between 3000 kg and 6000 kg as adults.",
    #     "Little red flying-fox (Pteropus scapulatus) lives in tropics and its diet is herbivorous.
    #     These animals can live up to 30 years, and they weigh between 0.3 kg and 0.6 kg as adults.",
    #     "Giraffe (Giraffa camelopardalis) lives in savannah and its diet is herbivorous.
    #     These animals can live up to 25 years, and they weigh between 1200 kg and 1800 kg as adults.",
    #     "Eurasian lynx (Lynx lynx) lives in temperate forest and its diet is carnivorous.
    #     These animals can live up to 7 years, and they weigh between 60 kg and 75 kg as adults.",
    #     "Brown bear (Ursus arctos) lives in temperate forest and its diet is omnivorous.
    #     These animals can live up to 33 years, and they weigh between 130 kg and 217 kg as adults."]

    print("Ecological Impact Score: {:.2f}".format(calculate_ecological_impact_score(animal_data)))
    # Expected output: Ecological Impact Score: 91.53
