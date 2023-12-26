"""
Loo funktsioon merge_lists(list1: list, list2: list) , mis võtab sisendina kaks listi ja
ühendab need üheks sorteeritud listiks.
"""
import itertools

def merge_lists(list1: list, list2: list):
    return sorted(list(itertools.chain(list1, list2)))

list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = merge_lists(list1, list2)
print(result) # [1, 2, 3, 4, 5, 6]