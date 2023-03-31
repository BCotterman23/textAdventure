#Make sure to first install colorama and termcolor to system via
#pip install colorama
#pip install termcolor

#import neccesary Modules
import time
import sys
from colorama import init
from termcolor import colored, cprint
init(autoreset= True)

#define variables
money = 0
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

#typing animation
def message(msg):

	for i in range(0, len(msg)):
	
		# printing each character of the message
		cprint(msg[i], end="")
		
		# adding time delay of half second
		time.sleep(0.04)


# main function

def start():
	stats()
	time.sleep(0.6)
	message("\nWelcome to the Game!")

start()