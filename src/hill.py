# Bintang Fajarianto
# NIM 13519138

# March 3, 2023

import numpy as np
from constant import ALPHABET, PLAIN_TEXT, HILL_KEY
from utils import remove_non_alphabet

# region Hill
class Hill:
  # used for decrypting cipher text
  def inverse_key(self, key: list):
    det = round(np.linalg.det(key)) % 26

    for i in range(1,26):
      if ((det * i) % 26 == 1):
        return (i * np.linalg.det(key) * np.linalg.inv(key)).round() % 26
    return None
  
  def encrypt(self, plain_text: str, key: list) -> str:
    # Make sure it's only 26 alphabet characters
    plain_text = remove_non_alphabet(plain_text)

    cipher_text = ""

    # add additional 'X' (uncommon repeated pair)
    # if the plain text is not a multiple of the key length
    while (len(plain_text) % len(key) != 0):
      plain_text += 'X'
    
    for idx in range(0, len(plain_text), len(key)):
      p = np.array([[ALPHABET.index(plain_text[idx + i])] for i in range(len(key))])
      c = np.array(key).dot(p) % 26

      cipher_text += "".join([ALPHABET[c[i][0]] for i in range(len(key))])

    return cipher_text

  def decrypt(self, cipher_text: str, key: list) -> str:
    # Make sure it's only 26 alphabet characters
    cipher_text = remove_non_alphabet(cipher_text)

    key_inv = self.inverse_key(key)
    plain_text = ""

    if (key_inv.all() == None):
      return 'Cannot decrypt using this key'

    for idx in range(0, len(cipher_text), len(key)):
      p = np.array([[ALPHABET.index(cipher_text[idx + i])] for i in range(len(key))])
      c = np.array(key_inv).dot(p) % 26

      plain_text += "".join([ALPHABET[int(c[i][0])] for i in range(len(key))])

    # remove 'X' (uncommon repeated pair) -> it might remove the original 'X' on plain text
    return plain_text.replace('X','')
# endregion Hill

if __name__ == "__main__":
  print("\n--- Hill ---")
  print(f"Plain Text: {PLAIN_TEXT}\nKey: {HILL_KEY}")
  hill_cipher_text = Hill().encrypt(PLAIN_TEXT, HILL_KEY)
  print(f"Encrypt result: {hill_cipher_text}")
  print(f"Decrypt result: {Hill().decrypt(hill_cipher_text, HILL_KEY)}")
