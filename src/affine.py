# Bintang Fajarianto
# NIM 13519138

# March 2, 2023

import string
from constant import ALPHABET
from utils import remove_non_alphabet

# region Affine
class Affine:
  def inverse_mod(self, key_m: int, base: int) -> int:
    for i in range(1, base):
      if ((key_m * i) % base) == 1:
        return i 
      
  def encrypt(self, plain_text: str, key_m: int, key_b: int):
    return "".join(
      map(
        lambda c_plain_text: ALPHABET[(ALPHABET.index(c_plain_text) * key_m + key_b) % 26],
        plain_text,
      )
    )

  def decrypt(self, cipher_text: str, key_m: int, key_b: int):
    return "".join(
      map(
        lambda c_cipher_text: ALPHABET[self.inverse_mod(key_m, len(ALPHABET)) * (ALPHABET.index(c_cipher_text) - key_b) % 26],
        cipher_text,
      )
    )
# endregion Affine


# Source: Kriptografi Klasik Bagian 4

print("\n--- Affine ---")
affine_plain_text = remove_non_alphabet("Kripto 123###")
affine_key_m = 7
affine_key_b = 1
print(f"Plain Text: {affine_plain_text}")
print(f"Key m: {affine_key_m}")
print(f"Key b: {affine_key_b}")
vigenere_cipher_text = Affine().encrypt(affine_plain_text, affine_key_m, affine_key_b)
print(f"Encrypt result: {vigenere_cipher_text}")
print(f"Decrypt result: {Affine().decrypt(vigenere_cipher_text, affine_key_m, affine_key_b)}")
