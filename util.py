import os
from time import sleep
def cr():
  return
  sleep(1)
  input("\nHit ENTER to continue.\n")
  os.system("clear")

def dramaticPrint(paytime):
  for letter in paytime:
    print(letter, end = "", flush=True)
    sleep(.15)
    if letter == ",":
      sleep(1)
  sleep(3)