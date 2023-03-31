#Make sure to first install colorama and termcolor to system via
#pip install colorama
#pip install termcolor
import time
import sys
from colorama import init
from termcolor import colored, cprint
init(autoreset= True)


money = 0
health = 5
hunger = 0

def stats():
    global health
    global hunger
    global money
    cprint(colored("Health", 'red') + ": [" + colored(str("*" * health), 'red') + str((10 - health)*"-") + "]", attrs=["bold"])
    time.sleep(0.1)
    cprint(colored("Hunger", 'black') + ": ["  + colored(str("*" * hunger), 'light_grey') + str((10 - hunger)*"-") + "]" , attrs=["bold"])
    cprint("Money: $" + str(money), 'green', attrs=["bold"])

stats()



# importing time module
import time


def message(string):

	for i in string:
	
		# printing each character of the message
		print(i, end="")
		
		# adding time delay of half second
		time.sleep(0.03)


# main function
if __name__ == '__main__':
	msg = "You wake up in a room. \nThere are no windows,  you don't know your name"
	
	# calling the function for printing the
	# characters with delay
	message(msg)
