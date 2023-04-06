# Bintang Fajarianto
# NIM 13519138

# March 1, 2023

import string
from utils import remove_non_alphabet

ALPHABET = string.ascii_lowercase

# region Vigenere
class Vigenere:
  # generate key by repeating the key until len(key) is equals len(text)
  def generate_repeating_key(self, text: str, key: str) -> str:
    return key * (len(text) // len(key)) + key[:len(text) % len(key)]
  
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
# endregion Vigenere

# region AutoKeyVigenere
class AutoKeyVigenere(Vigenere):
  # generate key by filling the key with the text until len(key) is equals len(text)
  def generate_auto_key(self, text: str, key: str) -> str:
    if len(text) > len(key):
      return key + text[:len(text) - len(key)]
    return key
  
  def encrypt(self, plain_text: str, key: str) -> str:
    return super().encrypt(plain_text, self.generate_auto_key(plain_text, key))

  def decrypt(self, cipher_text: str, key: str) -> str:
    list_key = list(key)
    list_plain_text = list()

    for idx in range(len(cipher_text)):
      c_plain_text = ALPHABET[(ALPHABET.index(cipher_text[idx]) + 26 - ALPHABET.index(list_key[idx])) % 26]
      list_plain_text.append(c_plain_text)
      list_key.append(c_plain_text)
    
    return "".join(list_plain_text)
# endregion AutoKeyVigenere



# Source: Kriptografi Klasik Bagian 3

print("\n--- Vigenere ---")
vigenere_plain_text = remove_non_alphabet("This Plain Text")
vigenere_key = remove_non_alphabet("###Sony123")
vigenere_cipher_text = Vigenere().encrypt(vigenere_plain_text, vigenere_key)
print(f"Plain Text: {Vigenere().decrypt(vigenere_cipher_text, vigenere_key)}")
print(f"Cipher Text: {vigenere_cipher_text}")

print("\n--- Auto Key Vigenere ---")
auto_key_vigenere_plain_text = remove_non_alphabet("This Plain Text")
auto_key_vigenere_key = remove_non_alphabet("###Sony123")
auto_key_vigenere_cipher_text = AutoKeyVigenere().encrypt(auto_key_vigenere_plain_text, auto_key_vigenere_key)
print(f"Plain Text: {AutoKeyVigenere().decrypt(auto_key_vigenere_cipher_text, auto_key_vigenere_key)}")
print(f"Cipher Text: {auto_key_vigenere_cipher_text}")
