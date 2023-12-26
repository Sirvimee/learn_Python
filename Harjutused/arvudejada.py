# Tagasta numbrite grupid.
from itertools import groupby
def find_repeated_numbers_groupby(numbers):
    repeated_nr_seq = []
    for key, group in groupby(numbers):
        #print(key, list(group))
        seq = list(group)
        if len(seq) > 1:
            repeated_nr_seq.append(seq)
    return repeated_nr_seq

numbers = [3,3,1,2,2,2,5,3,5,5,7,3,2,3,3,3,3,7,5]
print(find_repeated_numbers_groupby(numbers))

# Kiire sortimise operatsioon, kus numbrite järjekord jääb samaks
def quick_sort_operation(seq):
    left = [seq[i] for i in range(1, len(seq)) if seq[i] <= seq[0]]
    right = [seq[i] for i in range(1, len(seq)) if seq[i] > seq[0]]
    return left + [seq[0]] + right

seq = [5,7,2,3,8,11,1,5,6,4,9,10]
print(quick_sort_operation(seq))