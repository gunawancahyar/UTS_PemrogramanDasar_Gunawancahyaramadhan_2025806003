import re

def clean_text(text):
    # Menghapus karakter non-alfabet dan mengubah ke huruf kecil
    text = text.lower()
    return re.findall(r'\b\w+\b', text)

def count_vowels_consonants(text):
    vowels = "aeiou"
    v_count = 0
    c_count = 0
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count