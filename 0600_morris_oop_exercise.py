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

class Miner:
    def __init__(self):
        self.sleepiness = 0
        self.thirst = 0
        self.hunger = 0
        self.whisky = 0
        self.gold = 0

    def sleep(self):
        self.sleepiness -= 10   # update sleepiness
        self.thirst += 1    # update thirst
        self.hunger += 1   # update hunger
        # check for values out of boundaries

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold  += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1

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