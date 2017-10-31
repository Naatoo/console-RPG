from game.data.random_map.Map import MapNew
from game.data.random_map.Randomize_location import GenerateNPC, GenerateEnemies, GenerateItemsGround
from game.data.characters.Character import Player
from game.data.characters.Enemy import Enemy
from game.data.characters.NPC import NPC
from game.data.characters.equipment.Items import Item

from random import choice

class Game:
    def __init__(self):
        # ----------------------------------------
        # GENERATE CHARACTER
        # ----------------------------------------
        self.player = Player()
        self.if_icon_not_to_disappear = 0

        # ----
        # SPAWN CHARACTER
        m1 = MapNew()
        if m1.river_location == 5:
            m1.map[25] = "x"
            self.x = 25
        if m1.river_location == 4:
            m1.map[75] = "x"
            self.x = 75
        self.now_map = m1

        # ----------------------------------------
        # GENERATE NPC
        # ----------------------------------------
        self.NPC_spawn = GenerateNPC(
            self.now_map.river_location, self.now_map.mountain_location,
            self.now_map.city_location, self.now_map.village_location, self.now_map.sea_location)

        self.NPC_and_indexes = {
            "0": "Alchemist", "1": "Blacksmith", "2": "Cartographer",
            "3": "Innkeeper", "4": "Merchant", "5": "Guard",
            "6": "Monk", "7": "Innkeeper", "8": "Merchant"
            }
        # ----
        # SPAWN NPC
        self.alchemist = NPC("Alchemist", self.NPC_spawn.NPC[0])
        self.blacksmith = NPC("Blacksmith", self.NPC_spawn.NPC[1])
        self.cartographer = NPC("Cartographer", self.NPC_spawn.NPC[2])
        self.innkeeper_city = NPC("Innkeeper", self.NPC_spawn.NPC[3])
        self.merchant_city = NPC("Merchant", self.NPC_spawn.NPC[4])
        self.guard = NPC("Guard", self.NPC_spawn.NPC[5])
        self.monk = NPC("Monk", self.NPC_spawn.NPC[6])
        self.innkeeper_village = NPC("Innkeeper", self.NPC_spawn.NPC[7])
        self.merchant_village = NPC("Merchant", self.NPC_spawn.NPC[8])

        self.to_index_NPC = [
            self.alchemist, self.blacksmith, self.cartographer, self.innkeeper_city, self.merchant_city,
            self.guard, self.monk, self.innkeeper_village, self.merchant_village
            ]

        # ----------------------------------------
        # GENERATE ENEMIES
        # ----------------------------------------
        self.enemies_spawn = GenerateEnemies(
            self.now_map.river_location, self.now_map.mountain_location,
            self.now_map.city_location, self.now_map.village_location,
            self.now_map.sea_location, self.now_map.camp_location)

        self.enemies_and_indexes = {
            "0": ["b", "Bandit"], "1": ["s", "Skeleton"], "2": ["r", "Rat"],
            "3": ["O", "Giant"], "4": ["w", "Wolf"], "5": ["d", "Dwarf"],
            "6": ["c", "Cobra"], "7": ["h", "Hyaena"]
            }


        self.enemies_map = []
        [self.enemies_map.append("a") for i in range(100)]

        # ----
        # SPAWN ENEMIES
        for i in range(100):
            for k in range(4):
                if i in self.enemies_spawn.enemies[k]:
                    self.now_map.map[i] = self.enemies_and_indexes[str(k)][0]
                    self.enemies_map[i] = Enemy(self.enemies_and_indexes[str(k)][1])

        # ----------------------------------------
        # GENERATE ITEMS ON THE GROUND
        # ----------------------------------------
        self.items_map = []
        [self.items_map.append([]) for i in range(100)]

        self.misc_and_indexes = {
            "0": ["R", "Reed"], "1": ["P", "Potato"], "2": ["B", "Bottle of Water"],
            "3": ["A", "Apple"], "4": ["H", "Herb"]
            }

        self.items_spawn = GenerateItemsGround(
                self.now_map.river_location, self.now_map.mountain_location,
                self.now_map.city_location, self.now_map.village_location,
                self.now_map.sea_location)

        # ----
        # SPAWN ITEMS
        for i in range(100):
            for k in range(len(self.misc_and_indexes) - 4):
                if i in self.items_spawn.misc[k]:
                    self.items_map[i].append(Item(self.misc_and_indexes[str(k)][1]))
        # ----------------------------------------
        # GENERATE LIST OF FREE PLACES ON MAP FOR ENEMIES
        # ----------------------------------------
        self.occupied_x = []
        for item_type in self.items_spawn.misc:
            for item_x in item_type:
                self.occupied_x.append(item_x)

        for enemy_type in self.enemies_spawn.enemies:
            for enemy_x in enemy_type:
                self.occupied_x.append(enemy_x)

        free_x_for_enemies = []
        free_x_items = []
        signs = ["/", "=", "^", "~", "#", "x"]
        first_move = [self.x + 1, self.x - 1, 15, 18]
        for i in range(100):
            if self.now_map.map[i] not in signs and first_move:
                free_x_items.append(i)
            if self.now_map.map[i] not in signs and first_move and self.occupied_x:
                free_x_for_enemies.append(i)

        # ----
        # SPAWN THE REST OF ENEMIES
        enemies_rest_signs = ["w", "d", "c", "h"]
        for i in range(4):
            self.enemies_spawn.enemies.append([])
            for k in range(7):
                enemy_x = choice(free_x_for_enemies)
                self.now_map.map[enemy_x] = enemies_rest_signs[i]
                self.enemies_map[enemy_x] = Enemy(self.enemies_and_indexes[str(4 + i)][1])
                self.enemies_spawn.enemies[i + 4].append(enemy_x)
                free_x_for_enemies.remove(enemy_x)

        # ----------------------------------------
        # GENERATE LIST OF FREE PLACES ON MAP FOR ITEMS
        # ----------------------------------------
        for i in range(4):
            for k in range(10):
                item_x = choice(free_x_items)
                self.items_map[item_x].append(Item(self.misc_and_indexes[str(1 + i)][1]))

    def choose_direction(self, x, direction):
        index_changer = 0
        if direction == "w":
            index_changer = -10
        if direction == "s":
            index_changer = +10
        if direction == "a":
            index_changer = -1
        if direction == "d":
            index_changer = +1
        new_x = Game.move(self, x, index_changer)
        return new_x

    def check_possibility_to_move(self, x, check):
        try:
            # UNABLE TO MOVE IN RIVER, MOUNTAINS, SEA, WALL
            if self.now_map.map[check] in ["/", "=", "^", "~"]:
                return False
            # UNABLE TO GO AROUND MAP - RIGHT
            elif (x % 10) % 9 == 0 and check % 10 == 0 and x % 10 != 0:
                return False
            # UNABLE TO GO AROUND MAP - LEFT
            elif x % 10 == 0 and check < x:
                if check % 10 == 0:
                    return True
                return False
            # UNABLE TO GO AROUND MAP - UP AND DOWN
            elif check < 0 or check > 99:
                return False
            else:
                return True
        except IndexError:
            return False

    def move(self, x, index_changer):
        check = x + index_changer
        if Game.check_possibility_to_move(self, x, check):
            Game.add_and_remove_x(self, x, check)
            return check
        else:
            print("You cannot go there.")
            return x

    def add_and_remove_x(self, x, check):
        if self.if_icon_not_to_disappear == "#":
            self.now_map.map[x] = "#"
        else:
            self.now_map.map[x] = "O"
        self.if_icon_not_to_disappear = self.now_map.map[check]
        self.now_map.map[check] = "x"

    def check_if_able_to_fight(self, x):
        if self.enemies_map[x] != "a":
            return True
        return False

