
#     ----------------------------------------------------------------------------------------------------
#     |                                                                                                   |
#     |      Make sure to first install colorama and termcolor libraries via                              |
#     |      pip install colorama                                                                         |
#     |      pip install termcolor                                                                        |
#     |      if you can't access them due to school network policies                                      |
#     |      then get them from the github page https://github.com/BCotterman23/textAdventure             |
#     |      and run pip install Path/to/File                                                             |
#     ----------------------------------------------------------------------------------------------------


#import neccesary Modules
import time
import random
from colorama import init
from termcolor import colored, cprint
init(autoreset= True)


#define variables
money = 0
health = 10
hunger = 0
defense = 0
typingSpeed = 0.0
incorrect = 0

#define variables related to checkpoints
save = "start"
vault = "undiscovered"
yellTwoCheck = False
yellCheck = False
numpadCheck = False

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
    costs = [25 , 55 , 80 , 130 , 270]
    ArmorDurability = [1, 2.5 , 5 , 6]
    cprint("\n\nARMOR\n" , "blue")
    message("Armor " + chr(37) + " signifies the chance that it nullifies all incoming damage!\n")
    print("\n1. Plastic Chestplate - Made in China", end="")
    cprint(colored(" 10" + str(chr(37)) , "blue") +  colored(" -$25" , "green"))
    print("2. Leather Tunic - What's that smell? Wait... Isn't leather tanned in poop?", end="")
    cprint(colored(" 25" + str(chr(37)) , "blue") +  colored(" -$55" , "green"))
    print("3. Chainmail Chestplate - Wow! This stuff is heavy", end="")
    cprint(colored(" 40" + str(chr(37)) , "blue") +  colored(" -$80" , "green"))
    print("4. Diamond Chestplate - Wait... This is starting to feel like Minecraft", end="")
    cprint(colored(" 60" + str(chr(37)) , "blue") +  colored(" -$130" , "green"))
    print("5. Unobtanium Armor - \"This is why we're here; unobtanium, because this little gray rock sells for 20 million a kilo\"", end="")
    cprint(colored(" 80" + str(chr(37)) , "blue") +  colored(" -$270" , "green"))
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
    costs = [30 , 70 , 130]
    healthGained = [1 , 3, 6]
    cprint("\n\nMedPacks" , "red")
    print("1. Basic Medpack", end="")
    cprint(colored(" + 10 health" , "red") + colored(" -$30" , "green"))
    print("2. Medium Medpack", end="")
    cprint(colored(" + 30 health" , "red") + colored(" -$70" , "green"))
    print("3. Advanced MedPack", end="")
    cprint(colored(" + 60 health" , "red") + colored(" -$130" , "green"))
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

#sets up health check, manages hunger, and sets up fights
def healthCheck(timePasses):
      global health
      global typingSpeed
      global hunger
      global save
      global money
      global defense
      if timePasses == True:
           if hunger < 10:
                  hunger = hunger + 1
                  cprint("\n As time progresses, you grow more hungry")
                  cprint("\nHunger + 1", "red", "on_black")
           if hunger == 10:
                  num = random.randrange(1,11)
                  newDay = False
                  print(num)
                  if num < 5:
                        cprint(colored("You took 20 Damage because you are hungry!", "red", "on_black", attrs=["bold"]))
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

def fight(chance , damage):
      global defense
      global health
      global save
      print("")
      time.sleep(1)
      cprint("\nFIGHT INFO: " + str(chance*10) + chr(37) + " chance to take " + str(damage*10) + " damage.","red" ,"on_white", attrs=["bold"])
      for i in range(1,4):
            print("Fight begins in " + str(4-i) + ".")
            time.sleep(1)
      print("\nGo!\n")
      for i in range (0,5):
            cprint(".", "red", end="")
            time.sleep(1)
      x = random.randint(1,11)
      if x <= chance:
            health = health - damage
            cprint("\nYou have taken " + str(damage*10) + " damage.")
      else:
            cprint("\nLuckily, you avoided taking any damage", "green")
      healthCheck(False)
      eval(save)()

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
def functionInit(x, newDay):
      global save
      save = x
      if newDay == True:
            healthCheck(True)
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
      message("\nThe goal of the the game is survive to the end.\n")
      message("Once your health reaches 0, you die\n")
      message("Throughout the game, you will grow more hungry. Once your hunger is full, there is a 40" + chr(37) + " chance that you will take 20 damage the next day.\n")
      message("")
      message("Money will let you buy things such as food, armor, and MedKits in the shop\n")
      message("Your defense rating decreases the likelihood that you take damage.\n")
      message("For example, if your defense rating is 10% to dodge attacks, and the monster has a 30" + chr(27) +" chance to deal damage, your chance of taking damage will be 20%!\n")
      message("The shop can be accessed at any time by typing \"shop\" into the terminal")
      time.sleep(0.5)
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
      global vault
      if save != "yell":
            functionInit("yell", False)
      if yellCheck == False:
            message("\nYou decide to scream and yell. With no results, you decide to give up.")
            message("\nYou are exhausted from all of that yelling and decide to sit down for a minute")
            message("\nAs you are sitting down, you notice some weird markings on the floor. Upon further inspection, you realize that these markings appear to be in some sort of pattern.")
            message("\nThe markings read\n\n")
            time.sleep(0.1)
            cprint("II  III  V  IX   ____   XXXIII" , "white" ,"on_black" , attrs=["bold"])
            time.sleep(0.1)
            message("\n\nHmmmm. I wonder what those mean...")
            message("\nWhat will you do next?")
            time.sleep(0.1)
            if vault == "undiscovered":
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
                  message("\nGiven this knowledge, you go back to the numpad and try to figure out the pin\n")
                  numpad()
      else:
            yellTwo()

vault = "undiscovered"
def search():
      global save
      global vault
      global yellTwoCheck
      if save != "search":
            functionInit("search", False)
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
            functionInit("collectYourself", False)
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
            functionInit("cry", False)
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
            functionInit("yellTwo", False)
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
attempts = 0
def numpad():
      global attempts
      global save
      global yellCheck
      global numpadCheck
      attempts =  attempts + 1
      if attempts > 3:
            cprint("Hint: The terms are double of the previous term, minus 1. If you are not sure what than means. Maybe you should let out a little anger...", "red", attrs=["bold"])
      if save != "numpad":
            functionInit("numpad", False)
      if numpadCheck == False:
            message("\nYou walk up to the numpad. There are keys numbered 0-9 on the numpad. You notice a red LED illuminated above the keys")
            message("\nWhat number/s do you type in?")
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
            functionInit("climbToWindow", False)
      message("\nYou walk over to beneath the window and try to stick your fingers in the creacks between the bricks")
      message("\nYou start making your way up the wall")
      message("\nRight as you are about to reach the windowsill, you lose your footing, and fall\n")
      time.sleep(1)
      for i in range(0,20):
            print(str((i)*"a") + "ah!")
            time.sleep(0.02)
      health = health - 1
      message("\nOw, that hurt!\n")
      cprint("-1 Health", "red", "on_black" , attrs=["bold"])
      statsHealth()
      message("\nYou're not going to try that again.")
      message("\nWhat will you do next?")
      if vault == "undiscovered":
            print("\n1. cry")
            print("\n2. Search the room")
            response = input("\nInput:")
            if response == "1":
                  cry()
            elif response == "2":
                  search()
            else:
                  checkInputForSpecial(response)
      else:
            print("\n1. cry")
            print("\n2. Try to enter a number into the keypad ")
            response = input("\nInput:")
            if response == "1":
                  cry()
            elif response == "2":
                  numpad()
            else:
                  checkInputForSpecial(response)

#escape room
def vaultCorrect():
      global save
      if save != "vaultCorrect":
            functionInit("vaultCorrect", False)
      message("\nThe LED above the numpad flashes green")
      message("\nThe vault door unlocks with a satisfying click")
      message("\nYou pull the vault door open")
      message("\nYou immediately squint from all of the light. It's not sunny out, but you realize how dark that room was.")
      message("\nIt's warm and humid out. There seems to be a sort of electric buzz to the air.")
      message("\nIt appears that you are in some forested area.\n")
      message("\nYou have a weird sensation that you are being watched. You know you must find out more about this mysterious world\n\n")
      message("\nTwo roads diverge in a wood")
      time.sleep(0.3)
      message("\nAnd you, you took the path:")
      message("\n1.To the left: gravely and dark, it appears to be treacherous")
      message("\n2.To the right: appears to be the safer route")
      time.sleep(0.3)
      message("\nand it has made all the difference")      
      response = input("\nInput:")
      if response == "1":
            left()
      elif response == "2":
            right()
      else:
            checkInputForSpecial(response)

#left path
def left():
      global save
      if save != "left":
            functionInit("left", True)
      message("\nYou start to walk down the left path.")
      message("\nIt is a difficult path to walk on, but you decide to push on")
      message("\nAs you are walking along, you notice that there are signs warning you to turn back")
      message("\nThe path you are walking on is growing more and more overgrown")
      message("\nThen, in the middle of the trail, you see a skull, it appears to be human")
      message("\nWhat will you do?")
      print("\n1. Turn around")
      print("\n2. Continue to go forward")
      response = input("\nInput:")
      if response == "1":
            goBack()
      elif response == "2":
            continueOn()
      else:
            checkInputForSpecial(response)
      
def continueOn():
      global save
      if save != "continueOn":
            functionInit("continueOn", False)
      message("\nYou continue down the path.")
      message("\nIt is continueing to get more and more overgrown and dark.")
      message("\nThen, as you are keep moving, you hear movement up ahead.")
      message("\nwhat will you do?")  
      print("\n1. Turn around and go back")
      print("\n2. Continue forward")
      response = input("\nInput:")
      if response == "1":
            goBack()
      elif response == "2":
            continueOnTwo()
      else:
            checkInputForSpecial(response)

def goBack():
      message("\nYou decide to turn around and go back to the path that was on the right")
      rightPath()

def continueOnTwo():
      global save
      if save != "continueOnTwo":
            functionInit("continueOnTwo", False)
      message("\nDespite the scary signs, you decide to continue on.")
      message("\nAs you round the corner, you seen some sort of creature, it appears to be a cross between an ogre and a donkey\n")
      time.sleep(.25)
      cprint(colored("Hey! You there! Get over here!", "yellow", attrs=["bold"]) + " shouts the ogre hybrid")
      message("\nYou walk over to the ogre creature.\n")
      cprint(colored("So, I've been feeling a little bit bored", "yellow", attrs=["bold"]) + " says the ogre. " + colored("So, I've come up with some challenges for you.", "yellow", attrs=["bold"]))
      time.sleep(0.25)
      cprint(colored("\nIf you decide to participate in them, I will give you $10 for every challenge you complete. However, if you fail more than two of the challenges, you have to fight me. So, what do you say?", "yellow", attrs=["bold"]))
      print("\n1. \"I'm in!!!\"")
      print("\n2. \"Hell no!\"")
      response = input("\nInput:")
      if response == "1":
            challenges()
      elif response == "2":
            noChallenges()
      else:
            checkInputForSpecial(response)

def challenges():
      global save
      global money
      global incorrect
      incorrect = 0
      if save != "noChallenges":
            functionInit("noChallenges", False)
      message("\n\"I'll take the challenges\", you boldly say.")
      cprint("\nHa Ha Ha, brave of you puny human!", "yellow", attrs=["bold"])
      time.sleep(0.3)
      cprint("\nFor my first challenge, you must answer my riddle. I'll give you an easy one to start...", "yellow", attrs=["bold"])
      cprint("\nHow many months of the year have 28 days?")
      response = input("\nInput:")
      if response == "12" or response == "twelve" or response == "Twelve":
            money = money + 10
            cprint("\nFine, you got lucky with this one, but the next ones are going to get harder...", "yellow", attrs=["bold"])
            cprint("Money + 10", "green", attrs=["bold"])
            statsMoney()
      else:
            incorrect = incorrect + 1
            cprint("\nHa Ha Ha, you got it wrong, stupid! Just wait for my next riddle", "yellow", attrs=["bold"])
            cprint("\nThe answer was 12. All 12 months have 28 days or more in them", "yellow", attrs=["bold"])
      time.sleep(0.5)
      cprint("\nFor my next challenge, you must answer this.", "yellow", attrs=["bold"])
      cprint("\nWhere does today come before yesterday?")
      print("\nPlease write the one-word noun")
      response = input("\nInput:")
      if response == "dictionary" or response == "a dictionary" or response == "A dictionary" or response == "a Dictionary" or response == "Dictionary" or response == "in a dictionary" or response == "In a dictionary":
            money = money + 10
            cprint("\nWHAT!!!! How, did you get that?", "yellow", attrs=["bold"])
            cprint("Money + 10", "green", attrs=["bold"])
            statsMoney()
      else:
            incorrect = incorrect + 1
            cprint("\n Wow, you really are stupid!", "yellow", attrs=["bold"])
            cprint("\nThe answer was a dictionary.", "yellow", attrs=["bold"])
      time.sleep(0.5)
      checkForTwoIncorrect()
      cprint("\nFor my next challenge, you must answer this.", "yellow", attrs=["bold"])
      cprint("\nWhen my dad was 30, I was just 4 years old. Now his age is twice as old as my age. What is my present age?")


def checkForTwoIncorrect():
      global incorrect
      if incorrect >= 2:
            failedChallenges()


def failedChallenges():
      global save
      if save != "failedChallenges":
            functionInit("failedChallenges", False)
      cprint("\nYou have failed more than two challengrs. Now you must fight me!", "yellow", attrs=["bold"])
      time.sleep(1)
      cprint("FIGHT INFO: OGRE HAS 40" + chr(37) + " chance to deal 30hp of damage", "red", "on_white", attrs=["bold"])
      time.sleep(0.25)
      print("Remember, you have the chance to visit the shop at anytime via \"shop\", but you have been given a last chance to visit the shop before your fight. Please enter \"shop\" to visit the shop. Enter any other key to continue")
      response = input("\nInput:")
      if response == "shop":
            shop()
      else:
            save = "postFight"
            fight(4 , 3)
      


            

def noChallenges():
      global save
      if save != "noChallenges":
            functionInit("noChallenges", False)
      message("\n\"I don't think I want to participate,\" you say.")
      time.sleep(.75)
      cprint(colored("\nHa ha ha. TO BAD!!!", "yellow", attrs=["bold"]) + " Shouts the ogre " + colored("You have chosen to fight!", "yellow", attrs=["bold"]))
      time.sleep(1)
      cprint("FIGHT INFO: OGRE HAS 40" + chr(37) + " chance to deal 30hp of damage", "red", "on_white", attrs=["bold"])
      time.sleep(0.25)
      print("Remember, you have the chance to visit the shop at anytime via \"shop\", but you have been given a last chance to visit the shop before your fight. Please enter \"shop\" to visit the shop. Enter any other key to continue")
      response = input("\nInput:")
      if response == "shop":
            shop()
      else:
            save = "postFight"
            fight(4 , 3)


def postFight():
      global save
      if save != "postFight":
            functionInit("postFight", False)
      message("\nYou continue on, past the ogre. As you are walking, you realize just how much time has passed. There is a sense of urgency to find out what is going on. ")
      message("\nYou continue down the path. You have an odd feeling that something lies at the end of the path.")
      message("\nAs you continue down the path, you ")




#right path
def rightPath():
      global save
      if save != "rightPath":
            functionInit("rightPath", True)


fight(9,9)