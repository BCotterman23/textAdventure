

#import neccesary Modules
import time
import random
import sys

#random.randrange(0,100)

#define variables
money = 0
health = 10
hunger = 0
defense = 0
typingSpeed = 0.01
#typing animation
def message(msg):
     global typingSpeed
     for i in range(0, len(msg)):
          print(msg[i], end="")
          time.sleep(typingSpeed)
                
#stats dashboard
def stats():
    global health
    global hunger
    global money
    print("Health: ["  + (str("*" * health) + str((10 - health)*"-") + "]" + "     " , end="")
    time.sleep(0.4)
    print("Hunger: ["  + str("*" * hunger) + str((10 - hunger)*"-") + "]" + "     " , end="")
    time.sleep(0.4)
    print("Money: $" + str(money)+ "     ", end="")
    time.sleep(0.4)
    print("Defense: " + str(defense) + chr(37) + " Chance to dodge attacks")
    print("\n")

#shop 
def shop():
    global money
    global save
    print("\nWelcome to the Shop!")
    print("What would you like to buy?\n")
    print("Money: $" + str(money) + "     \n",)
    print("1. Food")
    print("2. Armor")
    print("3. Medpacks")
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
    print("\n\nFOOD")
    print("1. Twinkie - It's probably carcinogenic", end="")
    print(" + 10 food -$10")
    print("2. Ritz Cracker with slice of cheese- Cardboard with a little bit of salt", end="")
    print(" + 30 food -$25")
    print("3. Apple - An apple a day keeps the doctor away", end="")
    print(" + 50 food -$35")
    print("4. Bacon - Bacon takes good care of you.", end="")
    print(" + 60 food -$40")
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
    print("\n\nARMOR\n")
    message("Armor " + chr(37) + " signifies the chance that it nullifies all incoming damage!\n")
    print("\n1. Plastic Chestplate - Made in China", end="")
    print(" 10" + str(chr(37)) +  " -$25")
    print("2. Leather Tunic - What's that smell? Wait... Isn't leather tanned in poop?", end="")
    print(" 25" + str(chr(37)) + " -$55")
    print("3. Chainmail Chestplate - Wow! This stuff is heavy", end="")
    print(" 40" + str(chr(37)) +  " -$75")
    print("4. Diamond Chestplate - Wait... This is starting to feel like Minecraft", end="")
    print(" 60" + str(chr(37)) +  " -$110")
    print("5. Unobtanium Armor - \"This is why we're here; unobtanium, because this little gray rock sells for 20 million a kilo\"", end="")
    print(" 80" + str(chr(37)) +  " -$250"))
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
    print("\n\nMedPacks")
    print("1. Basic Medpack", end="")
    print(" + 10 health -$50")
    print("2. Medium Medpack", end="")
    print(" + 30 health -$100")
    print("3. Advanced MedPack", end="")
    print(" + 60 health -$175")
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
     message("\nWelcome to the Game!\n")
     message("This game utilizes a typing animation, if you'd like to disable the typing effect, please enter 0, if you would like to slow down the effect, enter a number greater that 0.01, likewise, if you'd like to speed it up, enter a number less than 0.01. If you like it at is is, enter 0.01")
     typingSpeed = float(input("\nInput:"))
     if typingSpeed > 0:
          message("Thanks, your typing speed is set to " + str(1/typingSpeed)+ " characters per second if you'd like to change this at any time, you can enter \"speed\" into the terminal\n")
     time.sleep(0.15)
     x = 0
     if x == 0:  
          start()
          x = 1
     else:
          save()

def start():
    global save
    global input
    save = start
    stats()
    time.sleep(0.6)
    message("\nWelcome to the Game!")
    message("The of the the game is survive to the end.\n")
    message("Once your health reaches 0, you die\n")
    message("Throughout the game, you will grow more hungry. Once your hunger is full, there is a 40" + chr(37) + " chance that you will take 20 damage the next day.\n")
    message("Money will let your buy things such as food, armor, and MedKits in the shop\n")
    message("Your defense rating decreases the likelihood that you take damage.\n")
    message("For example, if your defense rating is 10% to dodge attacks, and the monster has a 30" + chr(27) +" chance to deal damage, your chance of taking damage will be 20%!\n")
    message("The shop can be accessed at any time by typing \"shop\" into the terminal")
    time.sleep(0.2)
    message("\n\nYou wake up in an empty room. There are no windows, but there is a singular vault door across the room. ")
    message("\n You feel groggy, and disorented... \"What has happened\" you wonder. You try to think back to how you got here, but you have no memories")
    message("\n In fact, you can't even remember your name. All you know is that you have to escape this place")
    message("\n You take a quick glance around the room, there doesn't appear to be anything helpful, but it's a large room")
    message("So, you have a decicision to make, what are you going to do next?\n")
    time.sleep(.1)
    print("1. Yell, and hope that someone hears you, and can get you out")
    print("2. Search the room")
    print("3. Sarch yourself")
    print("4. Lie down on the floor and cry")
    response = input("\nInput:")
    


#functions related to decision 1

def yell():
     message("\nYou decide to scream and yell. With no results, you decide to give up.")
     message("test")

def death(newDay):
      global health
      global typingSpeed
      global hunger
      global save
      if newDay == 1:
           num = random.randrange(1,11)
           print(num)
           if num < 5:
                print("You took 20 Damage because your hunger is full!")
                health = health - 2
           else: 
                print("\n You have full hunger, but luckily didn't take damage")
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

death(1)           
init()
