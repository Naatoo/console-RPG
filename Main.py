from game.Game_Engine import GameMain
from copy import deepcopy

game = GameMain()

# MainMenu/save/load loop
saves = []
saves_names = []
while True:
    if game.end == 1:
        break

    if game.save == 1:
        game.save = 0
        name = input("give save's name: ")
        saves_names.append(name)
        saves.append(deepcopy(game))
        game.save = 0
        game.automatic_loop(game.x)

    if game.load == 1:
        if len(saves) == 0:
            print("You have no saves, try again.")
            break
        game.load = 0
        for save in saves_names:
            print(save)
        name = None
        while name not in saves_names:
            name = input("Type the save's name: ")
        for index, save in enumerate(saves_names):
            if name == save:
                game = saves[index]
        game.load = 0
        game.automatic_loop(game.x)



