from Equipment import Eq
from time import sleep


class Character:

    def __init__(self):
        StartingChoices.start(self)
        race = StartingChoices.beginning(self)
        self.strength = race["strength"]
        self.agility = race["agility"]
        self.capacity = race["capacity"]
        self.hp = race["hp"]
        self.hp_max = race["hp"]

        # GENERATE EQ
        self.Eq1 = Eq(self.capacity)


class StartingChoices(Character):
    def beginning(self):
        human_attributes = {"hp": 400, "strength": 10, "agility": 20, "capacity": 1300}
        orc_attributes = {"hp": 400, "strength": 15, "agility": 15, "capacity": 2000}
        elf_attributes = {"hp": 400, "strength": 5, "agility": 25, "capacity": 800}
        print("_" * 50)
        print("Which race would you like to play?")
        print("1. Human   ", human_attributes["hp"], "HP  ", human_attributes["strength"], "Strength  ",
              human_attributes["agility"], "Agility")
        print("2. Orc     ", orc_attributes["hp"], "HP  ", orc_attributes["strength"], "Strength  ",
              orc_attributes["agility"], "Agility")
        print("3. Elf     ", elf_attributes["hp"], "HP  ", elf_attributes["strength"], "Strength   ",
              elf_attributes["agility"], "Agility")
        print("_" * 50)
        sleep(1)
        print("HP shows how much hits you can stand.")
        sleep(1)
        print("Strength is responsible for your damage.")
        sleep(1)
        print("The higher agility you have the faster you attack.")
        print("_" * 50)
        user_choice = 0
        while user_choice not in ["1", "2", "3"]:
            user_choice = input("Type the number: ")
            if user_choice == "1":
                race = human_attributes
                return race
            if user_choice == "2":
                race = orc_attributes
                return race
            if user_choice == "3":
                race = elf_attributes
                return race

    def start(self):
        text = ["-" * 50,
                "Welcome in Natooland.",
                "-" * 50,
                "This world will not be kind for you.",
                "Fight with enemies and collect items.",
                "To win, you must find Giant's camp.",
                "Then you need to kill the beast."]
        for sentence in text:
            print(sentence)
            sleep(1)

    def first_move(self):
        text = ["You can see the map above.",
                "x is your position.",
                "You move using wasd buttons.",
                "w - Go north",
                "s - Go south",
                "a - Go west",
                "d - Go east",
                "Move in any direction (nothing is going to kill you there)."]
        for sentence in text:
            print(sentence)
            sleep(1)

    def insist_show_help(self):
        text = ["You can see how you moved.",
                "Now type h to see possible actions"]
        for sentence in text:
            print(sentence)
            sleep(1)
        help = 0
        while help != "h":
            help = input("Type h:")

    def second_move(self):
        text = ["Here you can see basic control buttons.",
                "You can always type h to see to possible moves.",
                "Type 0 to open save/load mode.",
                "This is how Natooland works.",
                "You should look for map in you want to see all the enemies.",
                "Be careful with rats nearby humans settlements.",
                "Look for some job in the city or in the village.",
                "You are on your own now.",
                "Good luck."]
        for sentence in text:
            print(sentence)
            sleep(1.5)
