class Item:
    def __init__(self, name):
        points = {
            "Reed": None,
            "Golden Key": None,
            "Sword": None,
            "Axe": None,
            "Map": None,
            "Teeth": None,
            "Potato": 50,
            "Bottle of Water": 60,
            "HP Potion": 100,
            "Strength Potion": 5,
            "Agility Potion": 5,
            "Silver Claymore": None,
            "Paw": None,
            "Bone Sword": None,
            "Rat Fur": None,
            "Wolf Fur": None
            }
        description = {
            "Reed": "A fresh reed.",
            "Golden Key": "It can open cooper locks.",
            "Sword": "A very sharp sword.",
            "Axe": "A double-edged axe.",
            "Map": "Shows locations of enemies.",
            "Teeth": 0,
            "Potato": "Restores HP.",
            "Bottle of Water": "Restores HP.",
            "HP Potion": "Increases HP.",
            "Strength Potion": "Increases Strength.",
            "Agility Potion": "Increases Agility.",
            "Silver Claymore": "A brand new claymore made of silver.",
            "Paw": 0,
            "Bone Sword": "You can feel it still lives.",
            "Rat Fur": "Very warm.",
            "Wolf Fur": "Very popular in winter."
            }
        value = {
            "Reed": 1,
            "Golden Key": 25,
            "Sword": 50, "Axe": 10,
            "Map": 100,
            "Teeth": 0,
            "Potato": 5, "Bottle of Water": 8,
            "HP Potion": 50,
            "Strength Potion": 50,
            "Agility Potion": 50,
            "Silver Claymore": 300,
            "Paw": 0,
            "Bone Sword": 500,
            "Rat Fur": 5,
            "Wolf Fur": 10
            }
        damage = {
            "Reed": None,
            "Golden Key": None,
            "Sword": 10,
            "Axe": 15,
            "Map": None,
            "Teeth": 5,
            "Potato": None,
            "Bottle of Water": None,
            "HP Potion": None,
            "Strength Potion": None,
            "Agility Potion": None,
            "Silver Claymore": 20,
            "Paw": 5,
            "Bone Sword": 30,
            "Rat Fur": None,
            "Wolf Fur": None
            }
        attack_speed = {
            "Reed": None,
            "Golden Key": None,
            "Sword": 5,
            "Axe": 5,
            "Map": None,
            "Teeth": 5,
            "Potato": None,
            "Bottle of Water": None,
            "HP Potion": None,
            "Strength Potion": None,
            "Agility Potion": None,
            "Silver Claymore": 6,
            "Paw": 7,
            "Bone Sword": 8,
            "Rat Fur": None,
            "Wolf Fur": None
            }
        is_weapon = {
            "Reed": 0,
            "Golden Key": 0,
            "Sword": 1,
            "Axe": 1,
            "Map": 0,
            "Teeth": 1,
            "Potato": 0,
            "Bottle of Water": 0,
            "HP Potion": 0,
            "Strength Potion": 0,
            "Agility Potion": 0,
            "Silver Claymore": 1,
            "Paw": 1,
            "Bone Sword": 1,
            "Rat Fur": 0,
            "Wolf Fur": 0
            }
        self.name = name
        self.value = value[name]
        self.points = points[name]
        self.damage = damage[name]
        self.attack_speed = attack_speed[name]
        self.is_weapon = is_weapon[name]
        self.description = description[name]