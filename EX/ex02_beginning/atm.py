"""
Create a machine that dispenses money using 1€, 5€, 10€, 20€, 50€ and 100€ banknotes.

Given the sum, one must print out how many banknotes does it take to cover the sum.
Task is to cover the sum with as little banknotes as possible.

Example
The sum is 72€
We use four banknotes to cover it. The banknotes are 20€, 50€, 1€ and 1€.
"""

amount = int(input("Enter a sum: "))
one_hundred_euros = amount // 100  # How many 100€ banknotes
fifty_euros = amount % 100 // 50  # How many 50€ banknotes
twenty_euros = amount % 100 % 50 // 20  # How many 20€ banknotes
ten_euros = amount % 100 % 50 % 20 // 10  # How many 10€ banknotes
five_euros = amount % 100 % 50 % 20 % 10 // 5  # How many 5€ banknotes
one_euros = amount % 100 % 50 % 20 % 10 % 5 // 1  # How many 1€ banknotes
banknotes = (str("100€, " * one_hundred_euros) +
             str("50€, " * fifty_euros) +
             str("20€, " * twenty_euros) +
             str("10€, " * ten_euros) +
             str("5€, " * five_euros) +
             str("1€, " * one_euros))

banknotes = banknotes.rstrip(', ')  # Remove comma and space at the end of the sentence

print(f"Amount of banknotes needed: {banknotes}")
