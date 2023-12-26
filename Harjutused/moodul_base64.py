"""
Loo funktsioon encode_and_decode_text(text: str), mis võtab sisendina teksti ja kodeerib selle base64 kodeeringusse
ning seejärel dekodeerib selle tagasi algtekstiks. Funktsioon peab tagastama kodeeritud ja dekodeeritud teksti ennikuna.
"""
import base64

def encode_and_decode_text(text: str):
    encoded_text = base64.b64encode(text.encode()).decode()
    decoded_text = base64.b64decode(encoded_text).decode()
    return (encoded_text, decoded_text)

text = "ITI0102 Programmeerimise algkursus (2023) on mu lemmik kursus!!!"
encoded, decoded = encode_and_decode_text(text)
print(encoded)
print(decoded)