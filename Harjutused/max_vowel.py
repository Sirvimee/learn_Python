# Leida täishäälik, mida esineb kõige rohkem
vowels = "euiüõaöä"
text = "adjkfsjaskjrjiugndffmnklsdklekaueirgjkKLjkl"
vow_dict = dict.fromkeys(vowels)
maximum = -1
max_vowel = ""
for key in vow_dict.keys():
    vow_dict[key] = text.count(key)
    if vow_dict[key] > maximum:
        maximum = vow_dict[key]
        max_vowel = key

print(max_vowel, maximum)