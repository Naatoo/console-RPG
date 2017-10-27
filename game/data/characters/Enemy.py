from game.data.characters.equipment.Equipment import Eq


class Enemy:
    def __init__(self, name):
        # dict = {
        #   enemy: [hp, strength, agility, capacity]
        #   }
        enemies = {
            "Bandit": (500, 8, 10, 1000),
            "Skeleton": [800, 5, 6, 500],
            "Rat": [200, 4, 10, 300],
            "Giant": [2000, 40, 5, 10000],
            "Wolf": [300, 5, 8, 1000],
            "Dwarf": [600, 15, 8, 1000],
            "Cobra": [250, 5, 20, 1900],
            "Hyaena": [300, 5, 18, 1000]
            }
        items = {
            "Bandit": ["Sword", "Reed"],
            "Skeleton": ["Bone Sword"],
            "Rat": ["Teeth", "Rat Fur"],
            "Giant": ["Axe"],
            "Wolf": ["Paw"],
            "Dwarf": ["Hammer"],
            "Cobra": ["Teeth"],
            "Hyaena": ["Teeth"]
           # "Potato": ["Wolf Fur"]
            }
        self.name = name
        self.hp = enemies[name][0]
        self.strength = enemies[name][1]
        self.agility = enemies[name][2]
        self.Equipment = Eq(enemies[name][3])
        for item in items[name]:
            self.Equipment.add_element(item)
