# Bintang Fajarianto
# NIM 13519138

# March 1, 2023

import string
from utils import remove_non_alphabet

ALPHABET = string.ascii_lowercase

class Vigenere:
  def encrypt(self, plain_text: str, key: str) -> str:
    return "".join(
      map(
        lambda c_plain_text, c_key: ALPHABET[(ALPHABET.index(c_plain_text) + ALPHABET.index(c_key)) % 26],
        plain_text,
        self.generate_repeating_key(plain_text, key)
      )
    )

  def decrypt(self, cipher_text: str, key: str) -> str:
    return "".join(
      map(
        lambda c_cipher_text, c_key: ALPHABET[(ALPHABET.index(c_cipher_text) + 26 - ALPHABET.index(c_key)) % 26],
        cipher_text,
        self.generate_repeating_key(cipher_text, key)
      )
    )
  
  def generate_repeating_key(self, text: str, key: str) -> str:
    return key * (len(text) // len(key)) + key[:len(text) % len(key)]
  
# Source: Kriptografi Klasik Bagian 3

print("\n--- Vigenere ---")
vigenere_plain_text = remove_non_alphabet("This Plain Text")
vigenere_key = remove_non_alphabet("###Sony123")
vigenere_cipher_text = Vigenere().encrypt(vigenere_plain_text, vigenere_key)
print(f"Plain Text: {Vigenere().decrypt(vigenere_cipher_text, vigenere_key)}")
print(f"Cipher Text: {vigenere_cipher_text}")
