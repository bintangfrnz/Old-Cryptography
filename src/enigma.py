# Bintang Fajarianto
# NIM 13519138

# March 4, 2023

from constant import ALPHABET
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
  enigma_plain_text = remove_non_alphabet("There is no time")
  enigma_steckerbrett = {'B':'A', ' ':' ', 'E':'Z'}
  enigma_alpha = 5
  enigma_beta = 17
  enigma_gamma = 24
  print(f"Plain Text: {enigma_plain_text}")
  print(f"Steckerbrett: {enigma_steckerbrett}")
  print(f"alpha: {enigma_alpha}")
  print(f"beta: {enigma_beta}")
  print(f"gamma: {enigma_gamma}")
  enigma_cipher_text = Enigma(enigma_steckerbrett, enigma_alpha, enigma_beta, enigma_gamma).encrypt(enigma_plain_text)
  print(f"Encrypt result: {enigma_cipher_text}")
  print(f"Decrypt result: {Enigma(enigma_steckerbrett, enigma_alpha, enigma_beta, enigma_gamma).decrypt(enigma_cipher_text)}")
