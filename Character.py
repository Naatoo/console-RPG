from Equipment import Eq


class Player:
    def __init__(self):
        race = self.beginning()
        self.strength = race["strength"]
        self.agility = race["agility"]
        self.capacity = race["capacity"]
        self.hp = race["hp"]
        self.hp_max = race["hp"]

        # GENERATE EQ
        self.Eq1 = Eq(self.capacity)
        items_start = ["Sword", "Potato", "Bottle of Water", "Bone Sword", "HP Potion", "Strength Potion"]
        for item in items_start:
            self.Eq1.add_element(item)

        # SET A WEAPON AS THE ONE NOW USED
        for item in self.Eq1.elements:
            if item.is_weapon == 1:
                item.is_weapon = 2
                break

    @staticmethod
    def beginning():
        human_attributes = {
            "hp": 400,
            "strength": 10,
            "agility": 20,
            "capacity": 1300
            }
        orc_attributes = {
            "hp": 400,
            "strength": 15,
            "agility": 16,
            "capacity": 2000
            }
        elf_attributes = {
            "hp": 400,
            "strength": 5,
            "agility": 25,
            "capacity": 800
            }
        print("_" * 50)
        print("Which race would you like to play?")
        print("1. Human   ", human_attributes["hp"], "HP  ",
              human_attributes["strength"], "Strength  ",
              human_attributes["agility"], "Agility")
        print("2. Orc     ", orc_attributes["hp"], "HP  ",
              orc_attributes["strength"], "Strength  ",
              orc_attributes["agility"], "Agility")
        print("3. Elf     ", elf_attributes["hp"], "HP  ",
              elf_attributes["strength"], "Strength   ",
              elf_attributes["agility"], "Agility")
        print("_" * 50)
        user_choice = 0
        while user_choice not in ["1", "2", "3"]:
            user_choice = input("Type the number: ")
            if user_choice == "1":
                race = human_attributes
                return race
            elif user_choice == "2":
                race = orc_attributes
                return race
            else:
                race = elf_attributes
                return race
