from time import sleep


class GameEnd:
    @staticmethod
    def ask_if_want_quit():
        text = [
            "-" * 50,
            "You did it! Do you want to finish game?",
            "Type 'end' to finish game or type '0' to continue playing in this world",
            "-" * 50,
        ]
        [GameEnd.print_and_sleep(line) for line in text]

    @staticmethod
    def game_quited():
        text = [
            "-" * 50,
            "Thank you for playing.",
            "Natoo 2017",
            "-" * 50,
        ]
        [GameEnd.print_and_sleep(line) for line in text]

    @staticmethod
    def game_finished():
        text = [
            "Congratulations.",
            "You have won.",
            "Natoo 2017."
        ]
        for i in range(10):
            GameEnd.print_and_sleep("*" * i)
        [GameEnd.print_and_sleep(line) for line in text]
        for i in range(10):
            GameEnd.print_and_sleep("*" * (10 - i))

    @staticmethod
    def print_and_sleep(sentence):
        print(sentence)
        sleep(0.8)
