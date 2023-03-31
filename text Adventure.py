money = 0
health = 1
hunger = 3


def stats():
    global health
    global hunger
    global money
    print("Health: [" + str("*" * health) + str((10 - health)*"-") + "]")
    print("Hunger: [" + str("*" * hunger) + str((10 - hunger)*"-") + "]")
    print("Money: $" + str(money))

stats()