
"""Opgave: Objektorienteret rollespil, afsnit 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
    _current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Del 2:
    Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.

Del 3:
    Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Del 4:
    Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
    Eksempel:  et hit reducerer _current_health ti_current_health=80 og attackpower=10:l 70.
    Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
    Definer derfor en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Del 5:
    Tilføj en klasse "Healer", som arver fra klassen Character.
    En healer har attackpower=0 men den har en ekstra attribut "healpower".

Del 6:
    Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
    For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
    tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du ikke aner, hvordan du skal begynde, kan du åbne 0622_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i 0624_rpg1_solution.py
"""

class Character:
    def __init__(self, name, max_health, _current_health, attackpower):
        self.name = name
        self.max_health = max_health
        self._current_health = _current_health
        self.attackpower = attackpower

    def __repr__(self):
        return F"Name: {self.name},\n Max health: {self.max_health}, Current health: {self._current_health}, Attack power: {self.attackpower}"

    def hit(self, other):
        other.get_hit(self)

    def get_hit(self, other):
        self._current_health -= other.attackpower

class Healer(Character):
    def __init__(self, name, max_health, _current_health, attackpower, healpower):
        super().__init__(name, max_health, _current_health, attackpower)
        self.healpower = healpower

    def __repr__(self):
        return F"Name: {self.name},\n Max health: {self.max_health}, Current health: {self._current_health}, Attack power: {self.attackpower}, Heal power: {self.healpower}"

    def heal(self, other):
        other.get_healed(self)

    def get_healed(self, other):
        self._current_health += other.healpower

ron = Character("Ron", 100, 100, 10)
bon = Character("Bon", 100, 100,  10)
ellen = Healer("Ellen", 90, 90, 0, 10)
ron.hit(bon)
print(bon)
ellen.heal(bon)
print(bon)