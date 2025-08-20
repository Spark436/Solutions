"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
."""


class miner()

def sleep():
    morris["sleepiness"] -= 10   # update sleepiness
    morris["thirst"] += 1    # update thirst
    morris["hunger"] += 1   # update hunger
    # check for values out of boundaries

def mine():
    morris["sleepiness"] += 5
    morris["thirst"] += 5
    morris["hunger"] += 5
    morris["gold"]  += 5

def eat():
    morris["sleepiness"] += 5
    morris["thirst"] -= 5
    morris["hunger"] -= 20
    morris["gold"] -= 2

def buy_whisky():
    morris["sleepiness"] += 5
    morris["thirst"] += 1
    morris["hunger"] += 1
    morris["whisky"] += 1
    morris["gold"] -= 1

def drink():
    morris["sleepiness"] += 5
    morris["thirst"] -= 15
    morris["hunger"] -= 1
    morris["whisky"] -= 1

def dead():
    return morris["sleepiness"] > 100 or morris["thirst"] > 100 or morris["hunger"] > 100


morris = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}  # dictionary

while not dead() and morris["turn"] < 1000:
    morris["turn"] += 1
    if morris["thirst"] >= 95:
        if morris["whisky"] == 0:
            buy_whisky()
        else:
            drink()
    elif morris["sleepiness"] >= 90:
        sleep()
    elif morris["hunger"] >= 93:
        eat()
    else:
        mine()

    print(morris)