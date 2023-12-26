"""
Kirjutage funktsioon compute_math_operations(number: float), mis võtab sisendina arvu ning tagastab selle
absoluutväärtuse ja ruutjuure float väärtustena.
"""

import math

def compute_math_operations(number: float) -> tuple:
    absolute_value = abs(number)
    square_root = math.sqrt(absolute_value)
    return (absolute_value, square_root)