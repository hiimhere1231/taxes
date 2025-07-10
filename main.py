from time import sleep
import os
import random
from colors import *
from ID import ID
import util
from pancake import Pancake
money = 47
valid = 0
bank = 0
global income
income = 0
dungeon = False
bankmoney = 0
permacount = 0


def street_performer(money, count, food):
  global income
  performance_quality = random.choice(['great', 'average', 'poor'])
  earnings = 0

  if performance_quality == 'great':
    earnings = 6
    print("You performed great! Earned $6.")
    util.cr()
  elif performance_quality == 'average':
    earnings = 4
    print("Your performance was average. Earned $4.")
    util.cr()
  else:
    earnings = 2
    print("Your performance was poor. Earned $2.")
    util.cr()
  income = 4
  money += checkCounter(count, money, income, food)
  return earnings
  
def freelance_artist(money, count, food):
  global income
  earnings = 0
  tasks = {'logo': 7, 'illustration': 10, 'poster': 5}
  print("Available tasks:")
  for task in tasks:
    print(f"{task}: ${tasks[task]}")

  choice = input("Choose a task: ")
  if choice in tasks:
    earnings = tasks[choice]
    print(f"You completed a {choice}! Earned ${earnings}.")
    
    util.cr()
  else:
    print("Invalid choice.")
    earnings = 0
  income = 7.50
  money += checkCounter(count, money, income, food)
  return earnings

def pet_sitter(money, count, food):
  global income
  tasks = ['feed', 'walk', 'play']
  task = random.choice(tasks)
  print(f"You need to {task} the pet.")
  
  util.cr()
  earnings = 0

  if task == 'feed':
    earnings = 8
  elif task == 'walk':
    earnings = 6
  else:  # play
    earnings = 7
  income = 7 
  print(f"Completed the {task} task. Earned ${earnings}.")
  
  util.cr()
  money += checkCounter(count, money, income, food)
  return earnings

def checkValid(valid):
  if valid == 7:
    print(f"Be absolutely sure that what your choosing is a {Red}valid{reset} option.")
    
    util.cr()
  if valid == 10:
    print(f"{Red}Why...{reset}")
    
    util.cr()
  if valid == 15:
    print(f"Stop messing around. {Red}The dungeon{reset} is still vacant.")    

def checkCounter(count, money, income, food):
  if count == 5:
    
    util.cr()
    paytime = (Red+"A week has passed, pay your taxes"+reset)
    util.dramaticPrint(paytime)
    
    util.cr()
    return income
  if food == 382:
    print("You died of starvation. Womp Womp")
    exit()
  if count >= 7:
    print(f"You have been sent to {Red}the dungeon.{reset}")
    
    util.cr()
    dungeon = True
    exit()
  if permacount == "365":
    ratesofinterest = bankmoney * 0.01
    return ratesofinterest
  return 0



def menu():
  print("𝕿𝖍𝖊 𝕯𝖚𝖓𝖌𝖊𝖔𝖓\n\n\t\t\t\t\t(っ◔◡◔)っ ♥ 𝓜 𝓔𝓝𝓤:\n\n\n𝓣𝓸𝓹𝓹𝓲𝓷𝓰𝓼:                           𝓟𝓪𝓷 𝓟𝓲 𝓚𝓲𝓵𝓲 𝓟𝓪𝓵𝓲𝓼𝓪:\n\n[C]hocochisps ~~~~~~~~~~ $362.91    [Bu]ttermilk ~~~~~~~~~ $497.23\n[B]ananas ~~~~~~~~~~~~~~ $181.83    [Who]le wheat ~~~~~~~~ $862.61\n[S]twarbery ~~~~~~~~~~~~ $276.26    [F]lour ~~~~~~~~~~~~~~ $467.33\n[Bl]euberry ~~~~~~~~~~~~ $209.24\n[W]hipped cream ~~~~~~~~ $222.46\n[Wh]ite chocolawaete ~~~ $952.30\n\n\n\n\tAʟʟ ᴘᴜʀᴄʜᴀsᴇs ᴍᴜsᴛ ʙᴇ ᴍᴀᴅᴇ ɪɴ ᴄᴀsʜ ᴀɴᴅ ᴡᴇ ᴡɪʟʟ ɴᴏᴛ ᴀᴄᴄᴇᴘᴛ ᴀɴʏᴛʜɪɴɢ ᴀʙᴏᴠᴇ ᴏʀ ʙᴇʟᴏᴡ ᴛʜᴇ ᴛᴏᴛᴀʟ ᴘʀɪᴄᴇ.")



print("You are living in a world named \""+Orange+"The Realm of the Sovereign Dominion"+reset+"\" (according to ChatGPT) Your ruler is "+Cyan+"Setheuthusus Bergesesesseses Biggest Sussy Ohioian Ragnor Joseph Yoseminai Buthman Yammir Apple and Bannanananana the CCCLIXXLV the IV"+reset+". Every week, you MUST pay $5 to your ruler, "+Cyan+"Setheuthusus Bergesesesseses Biggest Sussy Ohioian Ragnor Joseph Yoseminai Buthman Yammir Apple and Bannanananana the CCCLIXXLV the IV"+reset+". If you don't give payment, you will be sent to "+Red+"the dungeon"+reset+". Inside "+Red+"the dungeon"+reset+", you will live in "+Blue+"solitude"+reset+" for the rest of your life. You are only fed stwarberries, which taste like elephants, and to drink, you are given orange juice with extra pulp. However, when you behave, you are given orpple juice. You must eat and drink out of a "+Purple+"CELINE Dog Bowl In Lambskin With Triomphe Canvas"+reset+". You must use the bathroom inside an "+Green+"Extra Large Automatic Smart Kitty Litter Box, Self Cleaning Litter for Multiple Cats w/App Control, Low Noise"+reset+". In the corner of the dungeon, there is a "+Red+"wooden"+reset+" and "+Red+"rickety"+reset+" cage containing a "+Red+"lion"+reset+". The lion is fed and cared for well, but the person inside the dungeon does not know that. "+Red+"The dungeon"+reset+" is suspended over a "+Red+"shredder"+reset+" and the "+Red+"shredder"+reset+" is suspended over a pool of "+Red+"lava."+reset+" There is one window in the dungeon that is also the one window that is in the popular restaurant called \""+Grey+"𝕿𝖍𝖊 𝕯𝖚𝖓𝖌𝖊𝖔𝖓"+reset+"\n\"")
util.cr()
job = 4
while job > 3:
  job = input(f"As you only have {Green}${money}{reset}, you should probably get a job.\nThere are only three jobs in this kingdom so far. These jobs are are:\n[1] {Purple}Street perfromer{reset}\n[2] {Cyan}Freelance artist{reset}\n[3] {Orange}Pet sitter{reset}\nREMEMBER! This is an important choice and CANNOT be changed later on.\n")
  util.cr()
  if job.isalpha():
    print(f"Please choose a {Red}valid{reset} option.")
    
    util.cr()
    valid += 1
    job = 4
    continue
  job = int(job)
  if job > 3:
    print(f"Please choose a {Red}valid{reset} option.")
    
    util.cr()
    valid += 1
    continue
  elif job == 1:
    print("You are a street performer. You earn $4/week. You are employed by no one.")
    employer = "no one"
    
    util.cr()
  elif job == 2:
    print("You are a freelance artist. You earn $7.50/week. You are employed by no one.")
    employer = "no one"
    
    util.cr()
  else:
    print("You are a pet sitter. You earn $7/week. You are employed by Pet Go.")
    employer = "Pet Go"
    
    util.cr()
bank = 3
while bank > 2:
  bank = input(f"You must have a bank to store all your money.\nWould you like:\n[1] TD bank\n[2] Bank of America\n")
  util.cr()
  if bank.isalpha():
    print(f"Please choose a {Red}valid{reset} option.")
    
    util.cr()
    valid += 1
    bank = 3
    continue
  bank = int(bank)
  if bank > 2:
    print(f"Please choose a {Red}valid{reset} option.")
    
    util.cr()
    valid += 1
    continue
  elif bank == 1:
    bank = "td bank"
    break
  else:
    bank = "bank of america"
    break
print("You have joined the bank and have a %0.01/year interest rate.")

util.cr()
dragon = True
while dragon:
  password = input("Now that you've joined a bank, you need to make a password for your account! REMEMBER! It must be 3-8 characters long!\n")
  util.cr()
  if len(password) > 8:
    print("This password is too long.")
    util.cr()
    continue
  elif len(password) < 3:
    print("This password is too short.")
    util.cr()
    continue
  else:
    dragon = False
counter = 0
food = 0
print("Now that you've chose everything you need to, you may start living.")

# GAME LOOP
while True:
  print("You have: $"+str(money)+"\nWould you like to [1] "+Blue+"Work"+reset+" [2] "+Cyan+"Check ID"+reset+" [3] "+Orange+"Go to diner"+reset+" [4] "+Green+"Pay taxes"+reset+" or [5] "+Purple+"Bank"+reset)
  action = input()
  if action.isalpha():
    print(f"Please choose a {Red}valid{reset} option.")
    
    util.cr()
    valid += 1
    continue
  action = int(action)

  food += 1
  money += checkCounter(counter, money, income, food)
  names_2d_array = [
      ["Aiden", "Lila", "Ethan", "Sophie", "Mason", "Clara", "Noah", "Ivy", "Liam", "Ella", "Owen", "Nora", "Lucas", "Grace", "Henry", "Seth", "Peter"],  # First names
      ["Carter", "Montgomery", "Bennett", "Harrison", "Drake", "Donovan", "Weston", "Sullivan", "Carter", "Harper", "Blake", "Griffin", "Hayes", "Caldwell", "Lawson", "Berger"]  # Last names
  ]
  if action == 1:
    
    if job == 1:
      money += street_performer(money, counter, food)
      util.cr()
    elif job == 2:
      money += freelance_artist(money, counter, food)
      util.cr()
    else:
      money += pet_sitter(money, counter, food)
      util.cr()
  elif action == 2:
    RandFirstName = random.choice(names_2d_array[0])
    RandLastName = random.choice(names_2d_array[1])
    BigName = RandFirstName+" "+RandLastName
    thssn = random.randint(100000000, 999999999)
    thssn = str(thssn)

    thssn = thssn[:3] + "-" + thssn[3:]
    thssn = thssn[:6] + "-" + thssn[6:]
    streets = [[415, 736, 282, 953, 148, 674, 589, 392, 486, 809],
     ['Main St', 'Elm St', 'Maple Ave', 'Oak Dr', 'Pine Ln', 'Cedar Blvd', 'Birch Rd', 'Spruce St', 'Willow Way', 'Hickory Ct']]
    address = str(random.choice(streets[0]))
    adress = random.choice(streets[1])

    address = address+", "+adress
    birthday = str(random.randint(1, 10))
    stuID = str(random.randint(1000000, 9999999))
    id = ID(BigName, thssn, address, birthday, stuID, employer, income, bank)
    print(id)
    if BigName == "Seth Berger":
      print("You have became god.")
      money += 2345672345623456723464226454
    input("Press ENTER to exit\n")
  elif action == 3:
    menu()
    choice = input().lower()
    if choice == "c":
      if money < 362.91:
        print("You do not have enough money.")
        
        util.cr()
        continue
      else:
        money -= 362.91
        print("You ordered chocochisp pancakes.")
        
        util.cr()
        food = 0
    elif choice == "bu":
      if money < 497.23:
        print("You do not have enough money.")
        
        util.cr()
        continue
      else:
        money -= 497.23
        print("You ordered buttermilk pancakes.")
        
        util.cr()
        food = 0
    elif choice == "b":
      if money < 181.83:
        print("You do not have enough money.")
        
        util.cr()
        continue
      else:
        money -= 181.83
        print("You ordered banana pancakes.")
        
        util.cr()
        food = 0
    elif choice == "who":
      if money < 862.61:
        print("You do not have enough money.")
        
        util.cr()
        continue
      else:
        print("You ordered a whole wheat pancake.")
        
        util.cr()
        money -= 862.61
        food = 0
    elif choice == "s":
      if money < 276.26:
        print("You do not have enough money.")
        
        util.cr()
        continue
      else:
        money -= 276.26
        print("You ordered a stwarbery pancake.")
        
        util.cr()
        food = 0
    elif choice == "f":
      if money < 467.33:
        print("You do not have enough money.")
        
        util.cr()
        continue
      else:
        money -= 467.33
        print("You ordered a flour pancake.")
        food = 0
        
        util.cr()
    elif choice == "bl":
      if money < 209.24:
        print("You do not have enough money.")
        
        util.cr()
        continue
      else:
        money -= 209.24
        print("You ordered a bleuberry pancake.")
    elif choice == "w":
      if money < 222.46:
        print("You do not have enough money.")
        
        util.cr()
        continue
      else:
        print("You ordered a pancake with whipped cream.")
        money -= 222.46
        
        util.cr()
        food = 0
    elif choice == "wh":
      if money < 952.30:
        print("You do not have enough money.")
        
        util.cr()
        continue
      else:
        print("You ordered a white chocolawaete chip pancake.")
  elif action == 4:
    if counter != 6:
      counter += 1
      print("You cannot pay your taxes today.")
      
      util.cr()
      continue
    counter = 0
    id.taxes(money, income)
  elif action == "5":
    passtry = input("Please enter your password\n")
    if passtry != password:
      print("Incorrect! Please try again later.")
    elif passtry == password:
      deposit = input("would you like to make a [d]eposit or [w]ithdraw")
      if type(deposit) is int:
        print(f"Please choose a {Red}valid{reset} option next time.")
      elif deposit != "d" or deposit != "w":
        print(f"Please choose a {Red}valid{reset} option next time.")
      else:
        if deposit == "d":
          moeny = input("How much money would you like to deposit?\n")
          if deposit.isalpha():
            print(f"Please choose a {Red}valid{reset} option next time.")
          else:
            moeny = int(moeny)
            if moeny > money:
              print(f"Please choose a {Red}valid{reset} option next time.")
            else:
              money -= moeny
              bankmoney += moeny
  
        else:
          withdraw = input(f"You have {bankmoney} in your account.\nHow much money would you like to withdraw?\n")
          if int(withdraw) > bankmoney:
            print(f"Please choose a {Red}valid{reset} option next time.")
          else:
            money += int(withdraw)
            bankmoney -= int(withdraw)
  counter += 1
  permacount += 1
  util.cr()