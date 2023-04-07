# Bintang Fajarianto
# NIM 13519138

# March 1, 2023

from constant import ALPHABET, PLAIN_TEXT, KEY
from utils import remove_non_alphabet

# region Vigenere
class Vigenere:
  # generate key by repeating the key until len(key) is equals len(text)
  def generate_repeating_key(self, text: str, key: str) -> str:
    return key * (len(text) // len(key)) + key[:len(text) % len(key)]
  
  def encrypt(self, plain_text: str, key: str) -> str:
    # Make sure it's only 26 alphabet characters
    plain_text = remove_non_alphabet(plain_text)
    key = remove_non_alphabet(key)

    return "".join(
      map(
        lambda c_plain_text, c_key: ALPHABET[(ALPHABET.index(c_plain_text) + ALPHABET.index(c_key)) % 26],
        plain_text,
        self.generate_repeating_key(plain_text, key)
      )
    )

  def decrypt(self, cipher_text: str, key: str) -> str:
    # Make sure it's only 26 alphabet characters
    cipher_text = remove_non_alphabet(cipher_text)
    key = remove_non_alphabet(key)

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
    # Make sure it's only 26 alphabet characters
    plain_text = remove_non_alphabet(plain_text)
    key = remove_non_alphabet(key)

    return super().encrypt(plain_text, self.generate_auto_key(plain_text, key))

  def decrypt(self, cipher_text: str, key: str) -> str:
    # Make sure it's only 26 alphabet characters
    cipher_text = remove_non_alphabet(cipher_text)
    key = remove_non_alphabet(key)

    list_key = list(key)
    list_plain_text = ""

    for idx in range(len(cipher_text)):
      c_plain_text = ALPHABET[(ALPHABET.index(cipher_text[idx]) + 26 - ALPHABET.index(list_key[idx])) % 26]
      list_plain_text += c_plain_text
      list_key.append(c_plain_text)
    
    return "".join(list_plain_text)
# endregion AutoKeyVigenere

# region ExtendedVigenere
class ExtendedVigenere(Vigenere):
  def encrypt(self, plain_text: str, key: str) -> str:
    return "".join(
      map(
        lambda c_plain_text, c_key: chr((ord(c_plain_text) + ord(c_key)) % 256),
        plain_text,
        super().generate_repeating_key(plain_text, key)
      )
    )

  def decrypt(self, cipher_text: str, key: str) -> str:
    return "".join(
      map(
        lambda c_cipher_text, c_key: chr((ord(c_cipher_text) - ord(c_key)) % 256),
        cipher_text,
        super().generate_repeating_key(cipher_text, key)
      )
    )
# endregion ExtendedVigenere

if __name__ == "__main__":
  print("\n--- Vigenere ---")
  print(f"Plain Text: {PLAIN_TEXT}\nKey: {KEY}")
  vigenere_cipher_text = Vigenere().encrypt(PLAIN_TEXT, KEY)
  print(f"Encrypt result: {vigenere_cipher_text}")
  print(f"Decrypt result: {Vigenere().decrypt(vigenere_cipher_text, KEY)}")

  print("\n--- Auto Key Vigenere ---")
  print(f"Plain Text: {PLAIN_TEXT}\nKey: {KEY}")
  auto_key_vigenere_cipher_text = AutoKeyVigenere().encrypt(PLAIN_TEXT, KEY)
  print(f"Encrypt result: {auto_key_vigenere_cipher_text}")
  print(f"Decrypt result: {AutoKeyVigenere().decrypt(auto_key_vigenere_cipher_text, KEY)}")

  print("\n--- Extended Vigenere ---")
  print(f"Plain Text: {PLAIN_TEXT}\nKey: {KEY}")
  extended_vigenere_cipher_text = ExtendedVigenere().encrypt(PLAIN_TEXT, KEY)
  print(f"Encrypt result: {extended_vigenere_cipher_text}")
  print(f"Decrypt result: {ExtendedVigenere().decrypt(extended_vigenere_cipher_text, KEY)}")
