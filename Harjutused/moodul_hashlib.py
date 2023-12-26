"""Loo funktsioon calculate_md5_hash(text: str) , mis võtab sisendina teksti ja tagastab selle MD5 räsi."""

import hashlib

def calculate_md5_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()