# Bintang Fajarianto
# NIM 13519138

# March 3, 2023

import numpy as np
from re import findall
from collections import OrderedDict
from constant import ALPHABET, PLAIN_TEXT, KEY
from utils import remove_non_alphabet

# region Playfair
class Playfair:
  def generate_bigrams(self, text: str) -> list:
    modified_text = ""

    # separate two consecutive chars with 'X' (uncommon repeated pair)
    for i in range(1, len(text)):
      modified_text += text[i-1]
      if text[i] == text[i-1]:
        modified_text += 'X'    # better approach instead of using list and insert('x')
    modified_text += text[-1]
    
    # add char 'X' on the last of the modified text if it's is odd
    if (len(modified_text) % 2) == 1:
      modified_text += 'X'

    return findall('..', modified_text)

  def generate_table_key(self, key: str) -> list:
    list_key = "".join(OrderedDict.fromkeys(key.replace("J", "I"))) + "".join([c for c in ALPHABET if (c not in key) and (c != 'J')])
    return [list(text) for text in findall('.....', list_key)]
  
  def locate_position(self, key, first_ch: str, second_ch: str) -> dict:
     x1, y1 = np.where(np.array(key) == first_ch)
     x2, y2 = np.where(np.array(key) == second_ch)
     return {'x1': x1[0], 'y1': y1[0], 'x2': x2[0], 'y2': y2[0]}
  
  def encrypt(self, plain_text: str, key: str) -> str:
    # Make sure it's only 26 alphabet characters
    plain_text = remove_non_alphabet(plain_text)
    key = remove_non_alphabet(key)

    table_key = self.generate_table_key(key)
    cipher_text = ""

    for pair in self.generate_bigrams(plain_text):
      c_pos = self.locate_position(table_key, pair[0], pair[1])

      if (c_pos['x1'] == c_pos['x2']):
        cipher_text += (table_key[c_pos['x1']][(c_pos['y1'] + 1) % 5] + table_key[c_pos['x2']][(c_pos['y2'] + 1) % 5])
      elif (c_pos['y1'] == c_pos['y2']):
        cipher_text += (table_key[(c_pos['x1'] + 1) % 5][c_pos['y1']] + table_key[(c_pos['x2'] + 1) % 5][c_pos['y2']])
      else:
        cipher_text += (table_key[c_pos['x1']][c_pos['y2']] + table_key[c_pos['x2']][c_pos['y1']])
    return cipher_text
  
  def decrypt(self, cipher_text: str, key: str) -> str:
    # Make sure it's only 26 alphabet characters
    cipher_text = remove_non_alphabet(cipher_text)
    key = remove_non_alphabet(key)

    table_key = self.generate_table_key(key)
    plain_text = ""

    for idx in range(0, len(cipher_text), 2):
      c_pos = self.locate_position(table_key, cipher_text[idx], cipher_text[idx + 1])
      
      if (c_pos['x1'] == c_pos['x2']):
        plain_text += table_key[c_pos['x1']][(c_pos['y1'] - 1) % 5] + table_key[c_pos['x2']][(c_pos['y2'] - 1) % 5]
      elif (c_pos['y1'] == c_pos['y2']):
        plain_text += table_key[(c_pos['x1'] - 1) % 5][c_pos['y1']] + table_key[(c_pos['x2'] - 1) % 5][c_pos['y2']]
      else:
        plain_text += table_key[c_pos['x1']][c_pos['y2']] + table_key[c_pos['x2']][c_pos['y1']]
    
    # remove 'X' (uncommon repeated pair) -> it might remove the original 'X' on plain text
    return plain_text.replace('X','')
# endregion Playfair

if __name__ == "__main__":
  print("\n--- Playfair ---")
  print(f"Plain Text: {PLAIN_TEXT}\nKey: {KEY}")
  playfair_cipher_text = Playfair().encrypt(PLAIN_TEXT, KEY)
  print(f"Encrypt result: {playfair_cipher_text}")
  print(f"Decrypt result: {Playfair().decrypt(playfair_cipher_text, KEY)}")
