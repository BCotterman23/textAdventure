
#     ---------------------------------------------------------------------------
#     |                                                                         |
#     |      Make sure to first install colorama and termcolor libraries via    |
#     |      pip install colorama                                               |
#     |      pip install termcolor                                              |
#     |                                                                         |
#     ---------------------------------------------------------------------------


#import neccesary Modules
import time
import random
import sys
from colorama import init
from termcolor import colored, cprint
init(autoreset= True)


#define variables
money = 0
health = 10
hunger = 9
defense = 0
typingSpeed = 0.0

#define variables related to checkpoints
save = "start"
vault = "undiscovered"
yellTwoCheck = False
yellCheck = False
numpadCheck = False
yellOne = False



#typing animation
def message(msg):
     global typingSpeed
     for i in range(0, len(msg)):
          cprint(msg[i], end="")
          time.sleep(typingSpeed)
                

#stats dashboard
def stats():
    statsHealth()
    statsHunger()
    statsMoney()
    statsDefense()
    print("\n")

#Individualize stats
def statsHealth():
      global health
      cprint(colored("Health", 'red', "on_black") + ": [" + colored(str("*" * health), 'red') + str((10 - health)*"-") + "]" + "     " , attrs=["bold"] , end="")
      time.sleep(0.4)

def statsHunger():
      global hunger
      cprint(colored("Hunger", 'white', "on_black") + ": ["  + colored(str("*" * hunger), 'light_grey') + str((10 - hunger)*"-") + "]" + "     " , attrs=["bold"], end="")
      time.sleep(0.4)

def statsMoney():
      global money
      cprint(colored("Money: $" + str(money) , 'green', "on_black", attrs=["bold"] ) + "     ", end="")
      time.sleep(0.4)

def statsDefense():
      cprint("Defense: " + str(defense) + chr(37) + " Chance to dodge attacks", 'white', "on_black" , attrs=["bold"] )
      time.sleep(0.4)



#shop homepage 
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
         eval(save)()
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





# starting function
def init():
     global typingSpeed
     global save
     message("\nWelcome to the Game!\n")
     message("This game utilizes a typing animation, if you'd like to disable the typing effect, please enter 0, if you would like to slow down the effect, enter a number greater that 0.03, likewise, if you'd like to speed it up, enter a number less than 0.03. If you like it at is is, enter 0.03")
     message("\nNote that anything below 0.01 (other than 0) will not make a visible difference")
     speed = input("\nInput:")
     try:
       typingSpeed = float(speed)
     except ValueError:
            cprint("INVALID INPUT, TRY AGAIN" , "red", "on_black")
            init()
     if float(speed) > 0:
          typingSpeed = float(speed)
          message("Thanks, your typing speed is set to " + str(1/typingSpeed)+ " characters per second if you'd like to change this at any time, you can enter \"speed\" into the terminal\n")
     elif float(speed) == 0:
            typingSpeed = 0
            message("Disabled typing animation. If you'd like to change this at any time, you can enter \"speed\" into the terminal\n ")
     time.sleep(0.15)
     eval(save)()

#start of functions - print stats and save state
def functionInit(x):
      global save
      save = x
      stats()
      time.sleep(0.2)

      

#check input for "shop" , "speed", or invalid inputs
def checkInputForSpecial(x):
      global save
      if x == "speed":
            init()
      elif x == "shop":
            shop()
      else:
            cprint("INVALID INPUT, TRY AGAIN" , "red", "on_black")
            time.sleep(0.4)
            eval(save)()



def start():
      global save
      stats()
      time.sleep(0.6)
      message("\nWelcome to the Game!")
      message("\nThe of the the game is survive to the end.\n")
      message("Once your health reaches 0, you die\n")
      message("Throughout the game, you will grow more hungry. Once your hunger is full, there is a 40" + chr(37) + " chance that you will take 20 damage the next day.\n")
      message("Money will let your buy things such as food, armor, and MedKits in the shop\n")
      message("Your defense rating decreases the likelihood that you take damage.\n")
      message("For example, if your defense rating is 10% to dodge attacks, and the monster has a 30" + chr(27) +" chance to deal damage, your chance of taking damage will be 20%!\n")
      message("The shop can be accessed at any time by typing \"shop\" into the terminal")
      time.sleep(0.3)
      message("\n\nYou wake up in an empty room. There is a singular window located close to the ceiling, out of reach. There is also a vault door across the room. ")
      message("\nYou feel groggy and disorented... \"What has happened\" you wonder. You try to think back to how you got here, but you have no memories")
      message("\nIn fact, you can't even remember your name. All you know is that you have to escape this place")
      message("\nYou take a quick glance around the room, at a quick glance, there doesn't appear to be anything helpful.")
      message("\nSo, you have a decicision to make, what are you going to do next?\n")
      time.sleep(.1)
      print("1. Yell, and hope that someone hears you, and can get you out")
      print("2. Search the room")
      print("3. Take a minute to collect yourself")
      print("4. Cry")
      response = input("\nInput:")
      if response == "1":
            yell()
      elif response == "2":
            search()
      elif response == "3":
            collectYourself()
      elif response == "4":
            cry()
      else:
            checkInputForSpecial(response)




#functions related to round 1 of decisions

def yell():
      global save
      global yellCheck
      global numpadCheck
      if save != "yell":
            functionInit("yell")
      if yellCheck == False:
            message("\nYou decide to scream and yell. With no results, you decide to give up.")
            message("\nYou are exhausted from all of that yelling and decide to sit down for a minute")
            message("\nAs you are sitting down, you notice some weird markings on the floor. Upon further inspection, you realize that these markings appear to be in some sort of pattern.")
            message("\nThe markings read\n\n")
            time.sleep(0.1)
            cprint("II  III  V  IX       XXXIII" , "white" ,"on_black" , attrs=["bold"])
            time.sleep(0.1)
            message("\n\nHmmmm. I wonder what those mean...")
            message("\nWhat will you do next?")
            time.sleep(0.1)
            if numpadCheck == False:
                        print("\n1. Resume shouting")
                        print("\n2. Search the room")
                        print("\n3. Cry")
                        yellCheck = True
                        response = input("\nInput:")
                        if response == "1":
                              yellTwo()
                        elif response == "2":
                              search()
                        elif response == "3":
                              cry()
                        else:
                              checkInputForSpecial(response)
            else:
                  message("\nGiven this knowledge, you go back to the numpad and try to figure out the pin")
                  numpad()
      else:
            yellTwo()


vault = "undiscovered"
def search():
      global save
      global vault
      global yellTwoCheck
      if save != "search":
            functionInit("search")
      message("\nYou decide to take a moment and look around the room")
      message("\nYou walk to each corner of the room and look around for anything that may be of use. Unfortunately, you don't see anything.")
      message("\nYou walk over to the vault door. It is firmly locked. You take a look around the vault door and notice a keypad")
      message("\nWhat will you do?")
      vault = "discovered"
      if yellTwoCheck == False:
            print("\n1. Try to enter a number on the keypad")
            print("\n2. Yell and see if someone hears you")
            response = input("\nInput:")
            if response == "1":
                  numpad()
            elif response == "2":
                  yell()
            else:
                  checkInputForSpecial(response)
      else: 
            print("\n\n1. Try to enter a number on the keypad")
            print("2. Sit down and cry")
            response = input("\nInput:")
            if response == "1":
                  numpad()
            elif response == "2":
                  cry()
            else:
                  checkInputForSpecial(response)

def collectYourself():
      global save
      global money
      global collectMoney
      if save != "collectYourself":
            collectMoney = True
            functionInit("collectYourself")
      message("\nYou take a minute to collect yourself. As you are calming down, you notice there is a little weight in your back pocket")
      message("\nYou reach back to feel what is in your pocket, and pull out a small metallic disk, it appears to be a coin...\n")
      if collectMoney == True:
            time.sleep(0.4)
            cprint("Money +5      " , "green" , attrs=["bold"], end="")
            money = money + 5
            statsMoney()
            collectMoney = False
      else:
            print("\nYou have already collected the coin")
      print("\n\nWhat would you like to do next?")
      print("\n1. Yell for help")
      print("\n2. Search the room")
      print("\n3.Cry")
      response = input("\nInput:")
      if response == "1":
            yell()
      elif response == "2":
            search()
      if response == "3":
            cry()
      else:
            checkInputForSpecial(response)
            x = 1

def cry():
      global save
      global vault
      if save != "cry":
            functionInit("cry")
      message("You decide to cry but it doesn't make you feel any better")
      message(("\nWhat will you do next?"))
      print("\n1. Cry some more ")
      if vault == "undiscovered":
            print("\n2. Search the room")
            response = input("\nInput:")
            if response == "1":
                  cry()
            elif response == "2":
                  search()
            else:
                  checkInputForSpecial(response)
      else:
            print("\n2. Try to enter a number into the keypad ")
            response = input("\nInput:")
            if response == "1":
                  cry()
            elif response == "2":
                  numpad()
            else:
                  checkInputForSpecial(response)
      

#functions related to round 2 of decisions

def yellTwo():
      global save
      global vault
      global hunger
      global yellTwoCheck
      if save != "yellTwo":
            functionInit("yellTwo")
      if yellTwoCheck == False:
            yellTwoCheck = True
            message("\nYou decide to yell some more. By now, your throat is feeling sore and you decide to stop yelling for a while.")
            message("\nYou have been yelling for so long that you haven't noticed how the time has gone by until you notice that you are starting to grow hungry")
            hunger = hunger + 1
            time.sleep(0.3)
            cprint("\nHunger +1", "red", "on_black", attrs=["bold"])
            statsHunger()
            time.sleep(0.3)
            message("\nWhat will you do next?")
            if vault == "undiscovered":
                  print("\n1. Try and climb up to the window")
                  print("\n2. Search the room")
                  response = input("\nInput:")
                  if response == "1":
                        climbToWindow()
                  elif response == "2":
                        search()
                  else:
                        checkInputForSpecial(response)
            else:
                  print("\n1. Try and climb up to the window")
                  print("\n2. Try to enter a number into the keypad ")
                  response = input("\nInput:")
                  if response == "1":
                        climbToWindow()
                  elif response == "2":
                        numpad()
                  else:
                        checkInputForSpecial(response)
      else:
            message("\nWhat will you do next?")
            if vault == "undiscovered":
                  print("\n1. Try and climb up to the window")
                  print("\n2. Search the room")
                  response = input("\nInput:")
                  if response == "1":
                        climbToWindow()
                  elif response == "2":
                        search()
                  else:
                        checkInputForSpecial(response)
            else:
                  print("\n1. Try and climb up to the window")
                  print("\n2. Try to enter a number into the keypad ")
                  response = input("\nInput:")
                  if response == "1":
                        climbToWindow()
                  elif response == "2":
                        numpad()
                  else:
                        checkInputForSpecial(response)

def numpad():
      global save
      global yellCheck
      global numpadCheck
      if save != "numpad":
            functionInit("numpad")
      if numpadCheck == False:
            message("\nYou walk up to the numpad. There are keys numbered 0-9 on the numpad. You notice a red LED illuminated above the keys")
            message("\nWhat number do you type in?")
      response = input("\nPlease only enter numbers 0-9. There are no special characters\nInput:")
      #
      #Correct response is 17 
      #
      if response == "17":
            vaultCorrect()
      else:
            message("\nThe red LED flashes. You have entered an incorrect pin")
            message("\nWhat will you do next?")
            if yellCheck == False:
                  print("\n1. Try the pin again")
                  print("\n2. Yell in the hope that someone hears you")
                  response = input("\nInput:")
                  if response == "1":
                        numpad()
                  elif response == "2":
                        yell()
                  else:
                        checkInputForSpecial(response)
            else:
                  print("\n1.Try the pin again")
                  print("\n2. Remember the puzzle on the ground")
                  response = input("\nInput:")
                  if response == "1":
                        numpad()
                  elif response == "2":
                        message("\n You are remembering")
                        for i in range(0,6):
                              print(".")
                              time.sleep(.3)
                        cprint("II  III  V  IX       XXXIII" , "white" ,"on_black" , attrs=["bold"]) 
                  else:
                        checkInputForSpecial(response)
            
def climbToWindow():
      global save
      global health
      global yellTwoCheck
      global vault
      if save != "climbToWindow":
            functionInit("climbToWindow")
      message("\n You walk over to beneath the window and try to stick your fingers in the creacks between the bricks")
      message("\n You start making your way up the wall")
      message("\n Right as you are about to reach the windowsill, you lose your footing, and fall")
      for i in range(0,20):
            print(str((i)*"a") + "ah!")
            time.sleep(0.01)
      health = health - 1
      message("\nOw, that hurt!\n")
      cprint("-1 Health", "Red", "on_black" , attrs=["bold"])
      statsHealth()
      message("\n You decide that you're not going to try that again.")





      if yellTwoCheck == False:
            yellTwoCheck = True
            message("\nYou decide to yell some more. By now, your throat is feeling sore and you decide to stop yelling for a while.")
            message("\nYou have been yelling for so long that you haven't noticed how the time has gone by until you notice that you are starting to grow hungry")
            hunger = hunger + 1
            time.sleep(0.3)
            cprint("\nHunger +1", "red", "on_black", attrs=["bold"])
            statsHunger()
            time.sleep(0.3)
            message("\nWhat will you do next?")
            if vault == "undiscovered":
                  print("\n1. Try and climb up to the window")
                  print("\n2. Search the room")
                  response = input("\nInput:")
                  if response == "1":
                        climbToWindow()
                  elif response == "2":
                        search()
                  else:
                        checkInputForSpecial(response)
            else:
                  print("\n1. Try and climb up to the window")
                  print("\n2. Try to enter a number into the keypad ")
                  response = input("\nInput:")
                  if response == "1":
                        climbToWindow()
                  elif response == "2":
                        numpad()
                  else:
                        checkInputForSpecial(response)
      else:
            message("\nWhat will you do next?")
            if vault == "undiscovered":
                  print("\n1. Try and climb up to the window")
                  print("\n2. Search the room")
                  response = input("\nInput:")
                  if response == "1":
                        climbToWindow()
                  elif response == "2":
                        search()
                  else:
                        checkInputForSpecial(response)
            else:
                  print("\n1. Try and climb up to the window")
                  print("\n2. Try to enter a number into the keypad ")
                  response = input("\nInput:")
                  if response == "1":
                        climbToWindow()
                  elif response == "2":
                        numpad()
                  else:
                        checkInputForSpecial(response)






#escape room
def vaultCorrect():
      global save
      if save != "vaultCorrect":
            functionInit("vaultCorrect")









def deathCheck(newDay):
      global health
      global typingSpeed
      global hunger
      global save
      global money
      global defense
      if newDay == True:
           if hunger == 10:
                  num = random.randrange(1,11)
                  newDay = False
                  print(num)
                  if num < 5:
                        cprint(colored("You took 20 Damage because you are hungry!", "red", "on_black", attrs=["bold"]))
                        health = health - 2
                  else:
                        cprint(colored("\n You have full hunger, but luckily didn't take damage", "white" , attrs=["bold"]))
      if health > 1:
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
           time.sleep(1)
           print("\n Would you like to play again? Y/N")
           response = input("\nInput:")
           if response == "Y":
               print("\nStats Reset")
               health =  10
               hunger = 0
               money = 0
               defense = 0
               time.sleep(1)
               init()
           else:
                  print("Thanks for Playing")
      else: 
          save()
#start()
climbToWindow()