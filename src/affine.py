# Bintang Fajarianto
# NIM 13519138

# March 2, 2023

from constant import ALPHABET, PLAIN_TEXT, AFFINE_KEY_M, AFFINE_KEY_B
from utils import remove_non_alphabet

# region Affine
class Affine:
  def inverse_mod(self, key_m: int, base: int) -> int:
    for i in range(1, base):
      if ((key_m * i) % base) == 1:
        return i 
      
  def encrypt(self, plain_text: str, key_m: int, key_b: int):
    # Make sure it's only 26 alphabet characters
    plain_text = remove_non_alphabet(plain_text)
    
    return "".join(
      map(
        lambda c_plain_text: ALPHABET[(ALPHABET.index(c_plain_text) * key_m + key_b) % 26],
        plain_text,
      )
    )

  def decrypt(self, cipher_text: str, key_m: int, key_b: int):
    # Make sure it's only 26 alphabet characters
    cipher_text = remove_non_alphabet(cipher_text)

    return "".join(
      map(
        lambda c_cipher_text: ALPHABET[self.inverse_mod(key_m, len(ALPHABET)) * (ALPHABET.index(c_cipher_text) - key_b) % 26],
        cipher_text,
      )
    )
# endregion Affine

if __name__ == "__main__":
  print("\n--- Affine ---")
  print(f"Plain Text: {PLAIN_TEXT}\nKey m: {AFFINE_KEY_M}\nKey b: {AFFINE_KEY_B}")
  vigenere_cipher_text = Affine().encrypt(PLAIN_TEXT, AFFINE_KEY_M, AFFINE_KEY_B)
  print(f"Encrypt result: {vigenere_cipher_text}")
  print(f"Decrypt result: {Affine().decrypt(vigenere_cipher_text, AFFINE_KEY_M, AFFINE_KEY_B)}")
