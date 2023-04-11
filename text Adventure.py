#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     ---------------------------------------------------------------------------
#     |                                                                         |
#     |      Make sure to first install colorama and termcolor libraries via    |
#     |      pip install colorama                                               |
#     |      pip install termcolor                                              |
#     |                                                                         |
#     ---------------------------------------------------------------------------





#__________                                  __     __    
#\______   \  ____    ____    ____    ____ _/  |_ _/  |_  
# |    |  _/_/ __ \  /    \  /    \ _/ __ \\   __\\   __\ 
# |    |   \\  ___/ |   |  \|   |  \\  ___/ |  |   |  |   
# |______  / \___  >|___|  /|___|  / \___  >|__|   |__|   
#        \/      \/      \/      \/      \/               
                                                         
#  ________                                               
# /  _____/ _____     _____    ____    ______             
#/   \  ___ \__  \   /     \ _/ __ \  /  ___/             
#\    \_\  \ / __ \_|  Y Y  \\  ___/  \___ \              
# \______  /(____  /|__|_|  / \___  >/____  >             
#        \/      \/       \/      \/      \/              
                                                         




#import neccesary Modules
import time
import random
import sys
from colorama import init
from termcolor import colored, cprint
init(autoreset= True)

#random.randrange(0,100)

#define variables
money = 0
health = 10
hunger = 0
defense = 0
typingSpeed = 0.01
save = "start"
#typing animation
def message(msg):
     global typingSpeed
     for i in range(0, len(msg)):
          cprint(msg[i], end="")
          time.sleep(typingSpeed)
                
#stats dashboard
def stats():
    global health
    global hunger
    global money
    cprint(colored("Health", 'red', "on_black") + ": [" + colored(str("*" * health), 'red') + str((10 - health)*"-") + "]" + "     " , attrs=["bold"] , end="")
    time.sleep(0.4)
    cprint(colored("Hunger", 'white', "on_black") + ": ["  + colored(str("*" * hunger), 'light_grey') + str((10 - hunger)*"-") + "]" + "     " , attrs=["bold"], end="")
    time.sleep(0.4)
    cprint(colored("Money: $" + str(money) , 'green', "on_black", attrs=["bold"] ) + "     ", end="")
    time.sleep(0.4)
    cprint("Defense: " + str(defense) + chr(37) + " Chance to dodge attacks", 'white', "on_black" , attrs=["bold"] )
    print("\n")

#shop 
def shop():
    global money
    global save
    cprint("\nWelcome to the Shop!", 'yellow', attrs=["bold"])
    print("What would you like to buy?\n")
    cprint(colored("Money: $" + str(money) , 'green', "on_black", attrs=["bold"] ) + "     \n",)
    cprint("1. Food", "green")
    cprint("2. Armor" , "blue")
    cprint("3. Medpacks" , "red")
    print("4. Return to game")
    choice = input("\n")
    if choice == "1":
        food()
    elif choice == "2":
        armor()
    elif choice == "3":
        medPacks()
    elif choice == "4":
         save()
    else:
         shop()

#food part of shop
def food():
    global save
    global money
    global hunger
    costs = [10, 25, 35, 40]
    hungerQuenched = [1, 3 , 5 , 6]
    cprint("\n\nFOOD" , "green")
    print("1. Twinkie - It's probably carcinogenic", end="")
    cprint(colored(" + 10 food" , "red") + colored(" -$10" , "green"))
    print("2. Ritz Cracker with slice of cheese- Cardboard with a little bit of salt", end="")
    cprint(colored(" + 30 food" , "red") + colored(" -$25" , "green"))
    print("3. Apple - An apple a day keeps the doctor away", end="")
    cprint(colored(" + 50 food" , "red") + colored(" -$35" , "green"))
    print("4. Bacon - Bacon takes good care of you.", end="")
    cprint(colored(" + 60 food" , "red") + colored(" -$40" , "green"))
    print("5. Back to Shop")
    purchase = input("\n")
    purchase = int(purchase)
    if purchase == 5:
          shop()
    elif purchase < 5 and purchase > 0:
          if costs[purchase - 1] <= money:
                money = money - costs[purchase - 1]
                if hunger >= hungerQuenched[purchase - 1]:
                    hunger = hunger - hungerQuenched[purchase - 1]
                    print("You have satiated " + str(hungerQuenched[purchase-1]) + " hunger points\n")
                    stats()
                    shop()
                else:
                      print("You have satiated " + str(hunger*10) + " hunger points")
                      hunger = 0
                      stats()
                      shop()
          else: 
                print("Sorry, you don't have enough money\n")
                shop()
    else:
          print("INVALID INPUT")
          food()


#armor shop
def armor():
    global money
    global defense
    costs = [25 , 55 , 75 , 110 , 250]
    ArmorDurability = [1, 2.5 , 5 , 6]
    cprint("\n\nARMOR\n" , "blue")
    message("Armor " + chr(37) + " signifies the chance that it nullifies all incoming damage!\n")
    print("\n1. Plastic Chestplate - Made in China", end="")
    cprint(colored(" 10" + str(chr(37)) , "blue") +  colored(" -$25" , "green"))
    print("2. Leather Tunic - What's that smell? Wait... Isn't leather tanned in poop?", end="")
    cprint(colored(" 25" + str(chr(37)) , "blue") +  colored(" -$55" , "green"))
    print("3. Chainmail Chestplate - Wow! This stuff is heavy", end="")
    cprint(colored(" 40" + str(chr(37)) , "blue") +  colored(" -$75" , "green"))
    print("4. Diamond Chestplate - Wait... This is starting to feel like Minecraft", end="")
    cprint(colored(" 60" + str(chr(37)) , "blue") +  colored(" -$110" , "green"))
    print("5. Unobtanium Armor - \"This is why we're here; unobtanium, because this little gray rock sells for 20 million a kilo\"", end="")
    cprint(colored(" 80" + str(chr(37)) , "blue") +  colored(" -$250" , "green"))
    print("6. Back to Shop")
    purchase = input("\n")
    purchase = int(purchase)
    if purchase == 6:
          shop()
    elif purchase < 6 and purchase > 0:
          if costs[purchase - 1] <= money:
                money = money - costs[purchase - 1]
                defense = ArmorDurability[purchase-1]*10
                print("You have gained a " + str((ArmorDurability[purchase-1])*10) + chr(37) + " chance to dodge attacks")
                stats()
                shop()
          else: 
                print("Sorry, you don't have enough money\n")
                shop()
    else:
          print("INVALID INPUT")
          armor()


#medPacks Shop
def medPacks():
    global money
    global health
    costs = [50 , 100 , 175]
    healthGained = [1 , 3, 6]
    cprint("\n\nMedPacks" , "red")
    print("1. Basic Medpack", end="")
    cprint(colored(" + 10 health" , "red") + colored(" -$50" , "green"))
    print("2. Medium Medpack", end="")
    cprint(colored(" + 30 health" , "red") + colored(" -$100" , "green"))
    print("3. Advanced MedPack", end="")
    cprint(colored(" + 60 health" , "red") + colored(" -$175" , "green"))
    print("4. Back to Shop")
    purchase = input("\n")
    purchase = int(purchase)
    if purchase == 4:
          shop()
    elif purchase < 5 and purchase > 0:
          if costs[purchase - 1] <= money:
                money = money - costs[purchase - 1]
                if health + healthGained[purchase - 1] >= 10:
                    print("You have gained " + str(10 - health) + " health\n")
                    health = 10
                    stats()
                    shop() 
                else:
                    health = health + healthGained[purchase - 1]
                    print("You have gained " + str(healthGained[purchase-1]) + " health\n")
                    stats()
                    shop()
          else: 
                print("Sorry, you don't have enough money\n")
                shop()
    else:
          print("INVALID INPUT")
          medPacks()


          






# main function
def init():
     global typingSpeed
     global save
     save = init()
     message("\nWelcome to the Game!\n")
     message("This game utilizes a typing animation, if you'd like to disable the typing effect, please enter 0, if you would like to slow down the effect, enter a number greater that 0.01, likewise, if you'd like to speed it up, enter a number less than 0.01. If you like it at is is, enter 0.01")
     typingSpeed = float(input("\nInput:"))
     if typingSpeed > 0:
          message("Thanks, your typing speed is set to " + str(1/typingSpeed)+ " characters per second if you'd like to change this at any time, you can enter \"speed\" into the terminal\n")
     time.sleep(0.15)
     x = 0
     if x == 0:  
          save()
          x = 1
     else:
          save()

#start of functions
def functionInit(x):
      global save
      save = x
      stats()
      time.sleep(0.2)
      save()

#check input
def checkInputForSpecial(x):
      global save
      if x == "speed":
            init()
      elif x == "shop":
            shop()
      else:
            cprint("INVALID INPUT, TRY AGAIN" , "red", "on_black")
            time.sleep(0.4)
            save()



def start():
#      global input
      global save
      if save != "start":
            functionInit(start)
      time.sleep(0.6)
      message("\nWelcome to the Game!")
      message("The of the the game is survive to the end.\n")
      message("Once your health reaches 0, you die\n")
      message("Throughout the game, you will grow more hungry. Once your hunger is full, there is a 40" + chr(37) + " chance that you will take 20 damage the next day.\n")
      message("Money will let your buy things such as food, armor, and MedKits in the shop\n")
      message("Your defense rating decreases the likelihood that you take damage.\n")
      message("For example, if your defense rating is 10% to dodge attacks, and the monster has a 30" + chr(27) +" chance to deal damage, your chance of taking damage will be 20%!\n")
      message("The shop can be accessed at any time by typing \"shop\" into the terminal")
      time.sleep(0.3)
      message("\n\nYou wake up in an empty room. There are no windows, but there is a singular vault door across the room. ")
      message("\n You feel groggy and disorented... \"What has happened\" you wonder. You try to think back to how you got here, but you have no memories")
      message("\n In fact, you can't even remember your name. All you know is that you have to escape this place")
      message("\n You take a quick glance around the room, at a quick glance, there doesn't appear to be anything helpful.")
      message("So, you have a decicision to make, what are you going to do next?\n")
      time.sleep(.1)
      print("1. Yell, and hope that someone hears you, and can get you out")
      print("2. Search the room")
      print("3. Take a minute to collect yourself")
      print("4. Lie down on the floor and cry")
      response = input("\nInput:")
      if response == 1:
            yell()
      elif response == 2:
            search()
      elif response == 3:
            searchYourself()
      elif response == 4:
            lieDown()
      else:
            checkInputForSpecial(response)




#functions related to decision 1

def yell():
      global save
      if save != "yell":
            functionInit(yell)
      message("\nYou decide to scream and yell. With no results, you decide to give up.")
      message("\n You are exhausted from all of that yelling and decide to sit down for a minute")
      message("\n As you are sitting down, you notice some weird markings on the floor. Upon further inspection, you realize that these markings appear to be in some sort of pattern.")
      message("\n The markings read\n\n")
      time.sleep(0.1)
      cprint("II  III  V  IX       XXXIII" , "white" ,"on_black" , attrs=["bold"])
      time.sleep(0.1)
      message("\n\nHmmmm. I wonder what those mean...")
      message("\n What will you do next?")
      time.sleep(0.1)
      print("1. Resume shouting")
      print("2. Search the room")
      print("3. Cry")
      response = input("\nInput:")
      if response == 1:
            yellTwo()
      if response == 2:
            search()
      if response == 3:
            cry()
      if response == "shop":
            shop()
      else:
            save()


def search():
      global save
      if save != "search":
            functionInit(search)
      message("\nyou decide to take a moment and look around the room")
      message("\n You walk to each corner of the room and look around for anything that may be of use. Unfortunately, you don't see anything.")
      message("\n You walk over to the vault door. It is firmly locked. You take a look around the vault door and notice a keypad")
      message("What will you do?")














def death(newDay):
      global health
      global typingSpeed
      global hunger
      global save
      if newDay == 1:
           num = random.randrange(1,11)
           print(num)
           if num < 5:
                cprint(colored("You took 20 Damage because your hunger is full!", "red", "on_black", attrs=["bold"]))
                health = health - 2
           else: 
                cprint(colored("\n You have full hunger, but luckily didn't take damage", "white" , attrs=["bold"]))
      if health < 1:
           message("Sorry, You have died\n\n\n")
           typingSpeed = 0.005
           time.sleep(0.5)
           message(" ________  ________  _____ ______   _______           ________  ___      ___ _______   ________     \n")
           message("|\   ____\|\   __  \|\   _ \  _   \|\  ___ \         |\   __  \|\  \    /  /|\  ___ \ |\   __  \    \n")
           message("\ \  \___|\ \  \|\  \ \  \\\\\__\ \  \ \   __/|        \ \  \|\  \ \  \  /  / | \   __/|\ \  \|\  \   \n")
           message(" \ \  \  __\ \   __  \ \  \\\\|__| \  \ \  \_|/__       \ \  \\\\\  \ \  \/  / / \ \  \_|/_\ \   _  _\  \n")
           message("  \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \       \ \  \\\\\  \ \    / /   \ \  \_|\ \ \  \\\\  \| \n")
           message("   \ \_______\ \__\ \__\ \__\    \ \__\ \_______\       \ \_______\ \__/ /     \ \_______\ \__\\\\ _\ \n")
           message("    \|_______|\|__|\|__|\|__|     \|__|\|_______|        \|_______|\|__|/       \|_______|\|__|\|__|\n")
      else: 
          save()
