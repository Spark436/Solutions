"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import random

class Character:
    def __init__(self, name, max_health, _current_health, attackpower, attack_multiplier=1.0, mana=0, healpower=0, crit_chance=0.0, crit_damage=1.0, max_mana=0):
        self.name = name
        self.max_health = max_health
        self._current_health = _current_health
        self.attackpower = attackpower
        self.attack_multiplier = attack_multiplier
        self.mana = mana
        self.healpower = healpower
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.max_mana = max_mana

    def __repr__(self):
        return F"Name: {self.name},\n Max health: {self.max_health}, Current health: {self._current_health}, Attack power: {self.attackpower}"

    def hit(self, other, damage=None):
        if damage is None:
            damage = self.attackpower
        other.get_hit(self, damage)

    def get_hit(self, other, damage):
        self._current_health -= damage

    def get_healed(self, other):
        if self._current_health < 100:
            self._current_health += other.healpower

    def alive(self):
        return self._current_health > 0

    def respawn(self):
        self._current_health = self.max_health
        self.mana = self.max_mana

class Healer(Character):
    def __init__(self, name, max_health, _current_health, attackpower, healpower):
        super().__init__(name, max_health, _current_health, attackpower, healpower=healpower)

    def __repr__(self):
        return F"Name: {self.name},\n Max health: {self.max_health}, Current health: {self._current_health}, Attack power: {self.attackpower}, Heal power: {self.healpower}"

    def heal(self, other):
        other.get_healed(self)

    def action(self, other):
        # chooses one of the class actions and calls it
        pass

class Mage(Character):
    def __init__(self, name, max_health, _current_health, attackpower, attack_multiplier, mana, max_mana, crit_chance, crit_damage):
        super().__init__(name, max_health, _current_health, attackpower, attack_multiplier=attack_multiplier, mana=mana, max_mana=max_mana, crit_chance=crit_chance, crit_damage=crit_damage)

    def fireball(self, other,):
        damage = self.attackpower * self.attack_multiplier
        crit = random.random()
        if crit < self.crit_chance:
            damage *= self.crit_damage
        if self.mana >= 10:
            self.mana -= 10
            self.hit(other, damage)

    def meditate(self):
        self.mana += 60

    def hit(self, other, damage=None, mana_loss=None):
        if damage is None:
            damage = self.attackpower * 0.8
        other.get_hit(self, damage)

    def action(self, other): # chooses one of the class actions and calls it
        if self.mana < 10:
            self.meditate()
        else:
            if random.random() > 0.6:
                self.fireball(other)
            else:
                self.hit(other)

class Barbarian(Character):
    def __init__(self, name, max_health, _current_health, attackpower, attack_multiplier, crit_chance, crit_damage, self_damage, miss_chance):
        super().__init__(name, max_health, _current_health, attackpower, attack_multiplier=attack_multiplier, crit_chance=crit_chance, crit_damage=crit_damage)
        self.self_damage = self_damage
        self.miss_chance = miss_chance

    def blind_rage(self, other):
        if random.random() < self.miss_chance:
            damage = self.attackpower * 1.7
            crit = random.random()
            if crit < self.crit_chance:
                damage *= self.crit_damage
            self.hit(other, damage)
        else:
            print(self.name, "Missed")
        self_damage = self.self_damage
        self.get_hit(self, self_damage)

    def action(self, other): # chooses one of the class actions and calls it
        if random.random() > 0.5:
            self.blind_rage(other)
        else:
            self.hit(other)



ron = Character("Ron", 100, 100, 10)
bon = Character("Bon", 100, 100,  10)
ellen = Healer("Ellen", 90, 90, 0, 10)
wizzy = Mage("Wizzy", 80, 80, 10, 1.5, 100, 0.2, 1.2, 1.3)
bonkus = Barbarian("Bonkus",110, 110, 10, 1.3, 0.4, 1.5, 10, 0.6)

wizzy_wins = 0
bonkus_wins = 0

for x in range(100):
    wizzy.respawn()
    bonkus.respawn()

    while wizzy.alive() and bonkus.alive():
        if random.random() > 0.5:
            wizzy.action(bonkus)
            if bonkus.alive():
                bonkus.action(wizzy)
        else:
            bonkus.action(wizzy)
            if wizzy.alive():
                wizzy.action(bonkus)
    if wizzy.alive():
        wizzy_wins += 1
    else:
        bonkus_wins += 1

# ron.hit(bon)
# print(bon)
# ellen.heal(bon)
# print(bon)
# wizzy.fireball(bon)
# wizzy.fireball(bon)
# bonkus.blind_rage(bon)
print(wizzy_wins)
print(bonkus_wins)