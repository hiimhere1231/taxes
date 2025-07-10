class Pancake:
  def __init__(self, toppings, plain):
    list = ["chocochisps", "banana", "stwarbery", "bleuberry", "WHIPPED cream", "white chocolawaete chips"]
    pancakes = ["buttermilk", "whole wheat", "flour"]
    self.toppings = list[toppings]
    self.plain = pancakes[plain]
  def __str__(self):
    return str("Your pancake has "+self.toppings+" and it is made of "+self.plain)