# Leia pikim alamstring
def longest_unique_subsed(text):
    seq = ""
    longest_seq = ""
    for letter in text:
        if letter not in seq:
            seq += letter
        else:
            if len(seq) > len(longest_seq):
                longest_seq = seq
                seq = ""
    if len(seq) > len(longest_seq):
        longest_seq = seq

    return longest_seq


text = "abbbadefff"
print(longest_unique_subsed(text))