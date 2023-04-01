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
money = 10
health = 5
hunger = 0

#stats dashboard
def stats():
    global health
    global hunger
    global money
    cprint(colored("Health", 'red', "on_black") + ": [" + colored(str("*" * health), 'red') + str((10 - health)*"-") + "]" + "     " , attrs=["bold"] , end="")
    time.sleep(0.4)
    cprint(colored("Hunger", 'white', "on_black") + ": ["  + colored(str("*" * hunger), 'light_grey') + str((10 - hunger)*"-") + "]" + "     " , attrs=["bold"], end="")
    time.sleep(0.4)
    cprint("Money: $" + str(money), 'green', "on_black" , attrs=["bold"])
    time.sleep(0.4)

#shop 
def shop():
    cprint("Welcome to the Shop!", 'yellow', attrs=["bold"])
    print("What would you like to buy?\n")
    cprint("1. Food", "green")
    cprint("2. Armor" , "blue")
    cprint("3. Medpacks" , "red")
    cprint("4. Mystery Pack" , "magenta")
    print("5. Return to game")
    choice = input("\n")
    if choice == "1":
        food()

def food():
    global money
    global health
    costs = [10, 25, 35, 40]
    healthGained = [1, 3 , 5 , 6]
    cprint("\n\nFOOD" , "green")
    print("1. Twinkie - It's probably carcinogenic", end="")
    cprint(colored(" + 10 health" , "red") + colored(" -$10" , "green"))
    print("2. Ritz Cracker with slice of cheese- Cardboard with a little bit of salt", end="")
    cprint(colored(" + 30 health" , "red") + colored(" -$25" , "green"))
    print("3. Apple - An apple a day keeps the doctor away", end="")
    cprint(colored(" + 50 health" , "red") + colored(" -$35" , "green"))
    print("4. Bacon - Bacon takes good care of you.", end="")
    cprint(colored(" + 60 health" , "red") + colored(" -$40" , "green"))
    print("5. Back to Shop")
    purchase = input("\n")
    purchase = int(purchase)
    if purchase == 5:
          shop()
    elif purchase < 5 and purchase > 0:
          if costs[purchase - 1] <= money:
                money = money - costs[purchase - 1]
                health = health + healthGained[purchase - 1]
                print("You have gained " + str(healthGained[purchase-1]) + " hp")
                stats()
          else: 
                print("Sorry, you don't have enough money")
    else:
          print("INVALID INPUT")
          food()




shop()
#typing animation
def message(msg):

	for i in range(0, len(msg)):
	
		# printing each character of the message
		cprint(msg[i], end="")
		
		# adds rime delay
		time.sleep(0.03)


# main function

def start():
	stats()
	time.sleep(0.6)
	message("\nWelcome to the Game!")
	message("\nYou wake up in an empty room. There are no windows.")
