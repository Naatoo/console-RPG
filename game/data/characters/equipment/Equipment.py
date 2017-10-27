from game.data.characters.equipment.Items import Item


class Eq:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = []
        self.gold = 100

    def add_element(self, name):
        self.elements.append(Item(name))

    def remove_element(self, i):
        self.elements.pop(i)

    def remove_food(self, food_name):
        id = 0
        for item in self.elements:
            if item.name == food_name:
                self.elements.pop(id)
                return
            id += 1

    def sort_items_weapon(self):
        self.elements.sort(key=lambda x: x.is_weapon, reverse=True)

    def sort_items_eat_drink(self):
        for item in range(len(self.elements)):
            if self.elements[item].points is not None:
                self.elements.insert(0, self.elements.pop(item))

    def display_eq(self):
        self.sort_items_weapon()
        w = 0
        m = 0
        print("*" * 80)
        print("GOLD:", self.gold)
        print("*" * 80)
        for item in self.elements:
            # whether to make weapons overlay
            if item.is_weapon in [1, 2]:
                w += 1
            # whether to make items overlay
            if item.is_weapon == 0:
                m += 1

        id = 1
        # WEAPONS OVERLAY
        if w > 0:
            id = self.display_weapons(if_change=0)

        # ITEMS OVERLAY
        if m > 0:
            print("*" * 80)
            print("ITEMS")
            print("*" * 80)
            print("Item:           Value:   Description:")
        for item in self.elements:
            if item.is_weapon == 0:
                print(str(id) + ". ", end="")
                print(item.name, end="")
                print(" " * (16 - len(item.name)), end="")
                print(item.value, end="")
                print(" " * (9 - len(str(item.value))), end="")
                print(item.description)
                id += 1
        print("*" * 80)

    # SHOW WEAPONS (OR CHANGE WEAPON OPTION)
    def display_weapons(self, if_change):
        self.sort_items_weapon()
        print("*" * 80)
        print("WEAPONS")
        print("*" * 80)
        weapon_now = 0
        for item in self.elements:
            if item.is_weapon == 2:
                weapon_now = item.name
                print(item.name)
        if if_change == 1:
            print("- " * 40)
            print("You are now using", weapon_now.upper())
            print("- " * 40)
        print("*" * 80)
        print("Item:           Value:   Damage:   Attack speed: Description:")
        id = 1
        for item in self.elements:
            if item.is_weapon in [1,2]:
                print(str(id) + ". ", end="")
                print(item.name, end="")
                print(" " * (16 - len(item.name)), end="")
                print(item.value, end="")
                print(" " * (9 - len(str(item.value))), end="")
                print(item.damage, end="")
                print(" " * (10 - len(str(item.damage))), end="")
                print(item.attack_speed, end="")
                print(" " * (14 - len(str(item.attack_speed))), end="")
                print(item.description)
                id += 1
        print("*" * 80)
        return id

    def display_items_eat_drink(self):
        print("*" * 80)
        print("ITEMS TO CONSUME")
        print("*" * 80)
        number = 1
        for item in self.elements:
            if item.points is not None:
                print(number, end="")
                print(".", item.name)
                if item.name in ["Potato", "Bottle of Water", "Apple", "Hyaena's meet"]:
                    print("Restore HP ", end="")
                if item.name in ["HP Potion", "Herb"]:
                    print("Increase HP", end="")
                if item.name in ["Strength Potion"]:
                    print("Increase Strength by ", end="")
                if item.name in ["Agility Potion"]:
                    print("Increase Agility by ", end="")
                print(item.points)
                print("-" * 50)
                number += 1

    def items_names(self):
        names = []
        for i in range(len(self.elements)):
            names.append(self.elements[i].name)
        return names

