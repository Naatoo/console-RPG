class Eq:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = []
        self.gold = 100

    def add_element(self, name):
        self.elements.append(Item(name))

    def remove_element(self, i):
        self.elements.pop(i)

    def display_eq(self):
        w = 0
        m = 0
        print("*" * 80)
        print("GOLD:", self.gold)
        print("*" * 80)
        for i in range(len(self.elements)):
            if self.elements[i].is_weapon in [1,2]:
                w += 1
            if self.elements[i].is_weapon == 0:
                m += 1
        if w > 0:
            print("*" * 80)
            print("WEAPONS")
            print("*" * 80)
            print("Item:           Value:   Damage:   Attack speed: Description:")
        for i in range(len(self.elements)):
            if self.elements[i].is_weapon in [1,2]:
                print(self.elements[i].name, end="")
                print(" " * (16 - len(self.elements[i].name)), end="")
                print(self.elements[i].value, end="")
                print(" " * (9 - len(str(self.elements[i].value))), end="")
                print(self.elements[i].damage, end="")
                print(" " * (10 - len(str(self.elements[i].damage))), end="")
                print(self.elements[i].attack_speed, end="")
                print(" " * (14 - len(str(self.elements[i].attack_speed))), end="")
                print(self.elements[i].description)
        if m > 0:
            print("*" * 80)
            print("ITEMS")
            print("*" * 80)
            print("Item:           Value:   Description:")
        for i in range(len(self.elements)):
            if self.elements[i].is_weapon == 0:
                print(self.elements[i].name, end="")
                print(" " * (16 - len(self.elements[i].name)), end="")
                print(self.elements[i].value, end="")
                print(" " * (9 - len(str(self.elements[i].value))), end="")
                print(self.elements[i].description)
        print("*" * 80)

    def display_weapons(self):
        print("*" * 80)
        print("WEAPONS")
        print("*" * 80)
        weapon_now = 0
        for i in range(len(self.elements)):
            if self.elements[i].is_weapon == 2:
                weapon_now = self.elements[i].name
        print("-" * 50)
        print("You are now using", weapon_now.upper())
        print("-" * 50)
        print("*" * 80)
        print("Item:           Value:   Damage:   Attack speed: Description:")
        for i in range(len(self.elements)):
            if self.elements[i].is_weapon in [1,2]:
                print(self.elements[i].name, end="")
                print(" " * (16 - len(self.elements[i].name)), end="")
                print(self.elements[i].value, end="")
                print(" " * (9 - len(str(self.elements[i].value))), end="")
                print(self.elements[i].damage, end="")
                print(" " * (10 - len(str(self.elements[i].damage))), end="")
                print(self.elements[i].attack_speed, end="")
                print(" " * (14 - len(str(self.elements[i].attack_speed))), end="")
                print(self.elements[i].description)
        print("*" * 80)

    def display_items_eat_drink(self):
        n = 0
        for i in range(len(self.elements)):
            if self.elements[i].points != None:
                n += 1
        if n == 0:
            print("You don't have items to eat or drink")
            return
        print("*" * 80)
        print("ITEMS TO CONSUME")
        print("*" * 80)
        for i in range(len(self.elements)):
            if self.elements[i].points != None:
                print(i + 1, end="")
                print(".", self.elements[i].name)
                if self.elements[i].name in ["Potato", "Bottle of Water"]:
                    print("Restore HP ", end="")
                if self.elements[i].name in ["HP Potion"]:
                    print("Inncrease HP", end="")
                if self.elements[i].name in ["Strength Potion"]:
                    print("Increase Strength by ", end="")
                if self.elements[i].name in ["Agility Potion"]:
                    print("Increase Agility by ", end="")
                print(self.elements[i].points)
                print("-" * 50)

    def items_names(self):
        names = []
        for i in range(len(self.elements)):
            names.append(self.elements[i].name)
        return names


class Item:
    def __init__(self, name):
        points = {"Reed": None, "Golden Key": None, "Sword": None, "Axe": None, "Map": None,
                  "Teeth": None, "Potato": 50, "Bottle of Water": 60, "HP Potion": 100,
                  "Strength Potion": 5, "Agility Potion": 5, "Silver Claymore": None, "Paw": None,
                  "Bone Sword": None, "Rat Fur": None, "Wolf Fur": None}
        description = {"Reed": "A fresh reed.",
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
                       "Wolf Fur": "Very popular in winter."}
        value = {"Reed": 1, "Golden Key": 25, "Sword": 50, "Axe": 10,
                 "Map": 100, "Teeth": 0, "Potato": 5, "Bottle of Water": 8, "HP Potion": 50,
                 "Strength Potion": 50, "Agility Potion": 50, "Silver Claymore": 300, "Paw": 0,
                 "Bone Sword": 500, "Rat Fur": 5, "Wolf Fur": 10}
        damage = {"Reed": None, "Golden Key": None, "Sword": 10, "Axe": 15,
                  "Map": None, "Teeth": 5, "Potato": None, "Bottle of Water": None, "HP Potion": None,
                  "Strength Potion": None, "Agility Potion": None, "Silver Claymore": 20, "Paw": 5,
                  "Bone Sword": 30, "Rat Fur": None, "Wolf Fur": None}
        attack_speed = {"Reed": None, "Golden Key": None, "Sword": 5, "Axe": 5,
                        "Map": None, "Teeth": 5, "Potato": None, "Bottle of Water": None, "HP Potion": None,
                        "Strength Potion": None, "Agility Potion": None, "Silver Claymore": 6, "Paw": 7,
                        "Bone Sword": 8, "Rat Fur": None, "Wolf Fur": None}
        is_weapon = {"Reed": 0, "Golden Key": 0, "Sword": 1, "Axe": 1,
                     "Map": 0, "Teeth": 1, "Potato": 0, "Bottle of Water": 0, "HP Potion": 0,
                     "Strength Potion": 0, "Agility Potion": 0, "Silver Claymore": 1, "Paw": 1,
                     "Bone Sword": 1, "Rat Fur": 0, "Wolf Fur": 0}
        self.name = name
        self.points = points[name]
        self.description = description[name]
        self.value = value[name]
        self.damage = damage[name]
        self.attack_speed = attack_speed[name]
        self.is_weapon = is_weapon[name]
