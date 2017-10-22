from time import sleep


class Tutorial:
    @staticmethod
    def start_tutorial():
        text = [
            "-" * 50,
            "Welcome in Natooland.",
            "-" * 50,
            "This world will not be kind for you.",
            "Fight with enemies and collect items.",
            "To win, you must find Giant's camp.",
            "Then you need to kill the beast.",
            "-" * 50,
            "Now, choose your character.",
            "HP shows how much hits you can stand.",
            "Strength is responsible for your damage.",
            "The higher agility you have the faster you attack."
            ]
        [Tutorial.print_and_sleep(sentence) for sentence in text]

    @staticmethod
    def moving_guide():
        text = [
            "You can see the map above.",
            "x is your position.",
            "You move using wasd buttons.",
            "w - Go north",
            "s - Go south",
            "a - Go west",
            "d - Go east",
            "Move in any direction (nothing is going to kill you there)."
            ]
        [Tutorial.print_and_sleep(sentence) for sentence in text]

    @staticmethod
    def insist_on_showing_help():
        text = [
            "You can always type 'm' to see the map.",
            "Now, type 'h' to see other possible actions"
            ]
        [Tutorial.print_and_sleep(sentence) for sentence in text]
        help = 0
        while help != "h":
            help = input("Type h:")

    @staticmethod
    def final_text():
        text = [
            "Here you can see basic control buttons.",
            "You can always type h to see to possible moves.",
            "Type 0 to open save/load mode.",
            "You should look for map in you want to see all the enemies.",
            "Be careful with rats nearby humans settlements.",
            "Look for some job in the city or in the village.",
            "You are on your own now.",
            "Good luck."
            ]
        [Tutorial.print_and_sleep(sentence) for sentence in text]

    @staticmethod
    def print_and_sleep(sentence):
        print(sentence)
        sleep(0.8)

