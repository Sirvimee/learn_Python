import re
from collections import defaultdict

words = ["Tere", "sõber", "Tere", "tere", "armas", "sõber"]

indexes_dict = dict()
for i, word in enumerate(words):
    word_lower = word.lower()
    indexes_dict[word_lower] = indexes_dict.get(word_lower, []) + [i]
print(indexes_dict)

new_words = words[:]
for key, values in indexes_dict.items():
    if len(values) > 1:
        nr = 0
        for value in values:
            nr += 1
            new_words[value] = new_words[value] + "#" + str(nr)

print(new_words)


# kasutame regex sub-i
def number_repated_words(text):
    word_frequency = defaultdict(int)
    word_counter = defaultdict(int)
    pattern = r"[a-zA-ZüõöäÜÕÖÄ]+"

    words = re.findall(pattern, text)
    for word in words:
        word_frequency[word.lower()] += 1

    def replaced_word(match):
        word = match.group()
        if word_frequency[word.lower()] > 1:
            word_counter[word_lower()] += 1
            return word + "#" + str(word_counter[word_lower()])
        return word

    new_text = re.sub(pattern, replaced_word, text)
    return new_text


text = "Tere, sõber! Tere, tere armas sõber"
new_text = number_repated_words(text)
print(new_text)
