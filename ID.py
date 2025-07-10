from colors import *
from util import *

class ID:
  def __init__(self, name, ssn, address, birth, studentID, employer, income, bank):
    self.name = name
    self.ssn = ssn
    self.address = address
    self.birth = birth
    self.studentID = studentID
    self.employer = employer
    self.income = income
    self.bank = bank
  def __str__(self):
    return f"Name: {underline}{self.name}{reset}         Social Security Number: {underline}{self.ssn}{reset}\nAddress: {underline}{self.address}{reset}  \t  Date of Birth: {underline}{self.birth}{reset}         \nStudent ID: {underline}{self.studentID}{reset}"
  def taxes(self, money, income):
    skibidiToilet = 5/income
    print("Personal Information")
    name = input(f"{reset}Name: {underline}").lower()
    ssn = input(f"{reset}Social Security Number (SSN, type with \"-\"): {underline}").lower()
    address = input(f"{reset}Address: {underline}").lower()
    birth = input(f"{reset}Date of Birth (e.g. october 3rd 2011 would be 10 3 11): {underline}").lower()
    studentID = int(input(f"{reset}Student ID: {underline}").lower())
    employer = input(f"{reset}Employer: {underline}").lower()
    income = int(input(f"{reset}Income: {underline}").lower())
    bank = input(f"{reset}Bank: {underline}").lower()
    interest = input(f"{reset}Interest Income: {underline}").lower()
    print(f"{reset}Tax Calculation")
    print(f"{reset}Tax Rate: {skibidiToilet}%")
    tax = int(input(f"{reset}Estimated Tax Due (Taxable Income x Tax Rate): {underline}"))
    print(reset)
    cr()
    if name != name:
      print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
      dungeon = True
      exit()
    elif ssn != ssn:
      print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
      dungeon = True
      exit()
    elif address != address:
      print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
      dungeon = True
      exit()
    elif birth != birth:
      print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
      dungeon = True
      exit()
    elif studentID != studentID:
      print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
      dungeon = True
      exit()
    if job == 1:
      if employer != "no one":
        print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
        dungeon = True
        exit()
    elif job == 2:
      if employer != "no one":
        print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
        dungeon = True
        exit()
    elif job == 3:
      if employer != "pet go":
        print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
        dungeon = True
        exit()
    if income != income:
      print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
      dungeon = True
      exit()
    elif bank != bank:
      print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
      dungeon = True
      exit()
    elif interest != "0.01" or interest != ".01":
      print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
      dungeon = True
      exit()
    if tax != 5:
      print(f"You have made a mistake in your tax form and will be sent to {Red}the dungeon{reset}")
      dungeon = True
      exit()

