# Bintang Fajarianto
# NIM 13519138

# March 4, 2023

from constant import ALPHABET, PLAIN_TEXT, ENIGMA_STECKERBRETT, ENGIMA_ALPHA, ENGIMA_BETA, ENGIMA_GAMMA
from utils import remove_non_alphabet

# region Enigma
class Enigma:
  def __init__(self, steckerbrett = None, alpha = None, beta = None, gamma = None):
    self.alphabet = list(ALPHABET)

    # Steckerbrett is a sockets system that connects pairs of letters
    # that are interchanged between them.
    self.steckerbrett = {" " : " "} if (type(steckerbrett) is not dict) else steckerbrett

    if (alpha != None) and (beta != None) and (gamma != None):
      self.alpha = alpha
      self.beta = beta
      self.gamma = gamma

    else:
      # set all rotors to base states
      rotors = [self.alpha, self.beta, self.gamma]
      for rotor in rotors:
        rotor = 0 if (rotor == None) or (type(rotor) is not int) or (type(rotor) is not float) else rotor % 26
      self.alpha, self.beta, self.gamma = rotors
    
    # set the steckerbrett interchangeable and remove it from the alphabet
    for ch in list(self.steckerbrett.keys()):
      if ch in self.alphabet:
        self.alphabet.remove(ch)
        self.alphabet.remove(self.steckerbrett[ch])
        self.steckerbrett.update({self.steckerbrett[ch]:ch})
    
    # set the reflector
    self.reflector = [c for c in reversed(self.alphabet)]

  def permutate(self, rotor: int, inverse: bool = False) -> list:
    new_alphabet = list("".join(self.alphabet))

    if inverse:
      # rotate from first to last
      for _ in range(rotor):
        new_alphabet.append(new_alphabet.pop(0))
    else:
      # rotate from last to first
      for _ in range(rotor):
        new_alphabet.insert(0, new_alphabet.pop(-1))
          
    return new_alphabet
  
  def turning_rotor(self) -> None:
    self.alpha += 1
    if self.alpha % len(self.alphabet) == 0:
      self.beta += 1
      self.alpha = 0
    if self.beta % len(self.alphabet) == 0 and self.alpha % len(self.alphabet) != 0 and self.beta >= len(self.alphabet) - 1:
      self.gamma += 1
      self.beta = 1

  def encrypt(self, plain_text: str) -> str:
    # Make sure it's only 26 alphabet characters
    plain_text = remove_non_alphabet(plain_text)

    cipher_text = ""
    
    for ch in plain_text:
      # check if the letter exist in Steckerbrett
      if ch in self.steckerbrett:
        # encrypted into its pair
        cipher_text += self.steckerbrett[ch]
        
        # turning the rotors
        self.turning_rotor()

      # the letter not exist in Steckerbrett
      else:
        # forward
        # encrypted by 1st rotor
        c = self.permutate(self.alpha)[self.alphabet.index(ch)]
        # encrypted by 2nd rotor
        c = self.permutate(self.beta)[self.alphabet.index(c)]
        # encrypted by 3rd rotor
        c = self.permutate(self.gamma)[self.alphabet.index(c)]

        # return the inverse of current letter
        c = self.reflector[self.alphabet.index(c)]

        # backward
        # encrypted by 3rd rotor
        c = self.permutate(self.gamma, True)[self.alphabet.index(c)]
        # encrypted by 2nd rotor
        c = self.permutate(self.beta, True)[self.alphabet.index(c)]
        # encrypted by 1st rotor
        c = self.permutate(self.alpha, True)[self.alphabet.index(c)]
        
        cipher_text += c

        # turning the rotors
        self.turning_rotor()

    return cipher_text
  
  def decrypt(self, cipher_text: str) -> str:
    return self.encrypt(cipher_text)
# endregion Enigma

if __name__ == "__main__":
  print("\n--- Enigma ---")
  print(f"Plain Text: {PLAIN_TEXT}\nSteckerbrett: {ENIGMA_STECKERBRETT}\nalpha: {ENGIMA_ALPHA}\nbeta: {ENGIMA_BETA}\ngamma: {ENGIMA_GAMMA}")
  enigma_cipher_text = Enigma(ENIGMA_STECKERBRETT, ENGIMA_ALPHA, ENGIMA_BETA, ENGIMA_GAMMA).encrypt(PLAIN_TEXT)
  print(f"Encrypt result: {enigma_cipher_text}")
  print(f"Decrypt result: {Enigma(ENIGMA_STECKERBRETT, ENGIMA_ALPHA, ENGIMA_BETA, ENGIMA_GAMMA).decrypt(enigma_cipher_text)}")
