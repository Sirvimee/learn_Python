"""
Loo funktsioon search_text(pattern: str, text: str) ,
mis võtab sisendina otsingumustri ja teksti ning tagastab leitud vastete listi.
"""

import re

def search_text(pattern: str, text: str) -> list:
    return re.findall(pattern, text)

"""
Kirjuta funktsioon extract_numbers_from_text(text: str), mis võtab sisendina teksti ja kasutab regulaaravaldist 
(re moodul) leidmaks kõikides numbreid sisaldavates sõnedes olevad arvud. Funktsioon peab tagastama need arvud listina.
"""
import re

def extract_numbers_from_text(text: str) -> list:
    return list(map(int, re.findall(r'\d+', text)))

numbered_text = "Kui ma vaid 5 saaks selle aine... 829349872349870239847298374"
numbers = extract_numbers_from_text(numbered_text)
print(numbers) # [5, 829349872349870239847298374]