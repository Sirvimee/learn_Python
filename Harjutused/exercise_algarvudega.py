"""
Lahuta etteantud täisarv algarvudeks.
"""


nr = 10000000

flag = False
factors = []

for i in range(2, nr):
    while nr % i == 0:
        factors.append(i)
        nr /= i
        flag = True

    if nr == 1:
        break

if not flag:
    print([nr])
else:
    print(factors)
