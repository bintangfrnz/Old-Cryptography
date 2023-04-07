# Bintang Fajarianto
# NIM 13519138

# March 1, 2023

from re import sub

def remove_non_alphabet(text: str) -> str:
  return sub(r'[^A-Z]', '', text.upper())
