#Make sure to first install colorama and termcolor to system via
#pip install colorama
#pip install termcolor

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
health = 6
hunger = 3
defense = 0
save = 0

#typing animation
def message(msg):

	for i in range(0, len(msg)):
	
		# printing each character of the message
		cprint(msg[i], end="")
		
		# adds rime delay
		time.sleep(0.01)
                
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
    cprint("Welcome to the Shop!", 'yellow', attrs=["bold"])
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

def start():
    stats()
    time.sleep(0.6)
    message("\nWelcome to the Game!")
    message("\nYou wake up in an empty room. There are no windows.")


start()