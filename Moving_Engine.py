from Character import Player
from Map import MapNew
from Generate_objects_indexes import GenerateNPC, GenerateEnemies
from Enemy import NPC


class Game:
    def __init__(self):
        # GENERATE CHARACTER
        self.player = Player()
        self.player.Eq1.add_element("Sword")
        self.player.Eq1.add_element("Potato")
        self.player.Eq1.add_element("Sword")
        self.player.Eq1.add_element("Potato")
        self.player.Eq1.add_element("Sword")
        self.player.Eq1.add_element("Axe")
        self.player.Eq1.add_element("Potato")
        self.player.Eq1.add_element("Axe")
        for i in range(len(self.player.Eq1.elements)):
            if self.player.Eq1.elements[i].is_weapon == 1:
                self.player.Eq1.elements[i].is_weapon = 2
                break
        self.player.Eq1.add_element("Potato")
        self.player.Eq1.add_element("Bottle of Water")
        self.if_icon_not_to_disappear = 0

        # SPAWN CHARACTER
        m1 = MapNew()
        if m1.river_location == 5:
            m1.map[25] = "x"
            self.x = 25
        if m1.river_location == 4:
            m1.map[75] = "x"
            self.x = 75
        self.now_map = m1

        # GENERATE ENEMIES
        self.enemies_spawn = GenerateEnemies(
            self.now_map.river_location, self.now_map.mountain_location,
            self.now_map.city_location, self.now_map.village_location,
            self.now_map.sea_location, self.now_map.camp_location)
        self.enemies_and_indexes = {"0": ["b", "Bandit"], "1": ["s", "Skeleton"], "2": ["r", "Rat"],
                                    "3": ["O", "Giant"], "4": ["w", "Wolf"]}

        # SPAWN ENEMIES
        for i in range(100):
            for k in range(len(self.enemies_and_indexes) - 1):
                if i in self.enemies_spawn.enemies[k]:
                    self.now_map.map[i] = self.enemies_and_indexes[str(k)][0]

        # GENERATE NPC
        self.NPC_spawn = GenerateNPC(
            self.now_map.river_location, self.now_map.mountain_location,
            self.now_map.city_location, self.now_map.village_location, self.now_map.sea_location)
        self.NPC_and_indexes = {"0": "Alchemist", "1": "Blacksmith", "2": "Cartographer", "3": "Innkeeper",
                                "4": "Innkeeper", "5": "Merchant", "6": "Merchant", "7": "Guard", "8": "Monk"}
        self.alchemist = NPC("Alchemist", self.NPC_spawn.NPC[0])
        self.blacksmith = NPC("Blacksmith", self.NPC_spawn.NPC[1])
        self.cartographer = NPC("Cartographer", self.NPC_spawn.NPC[2])
        self.innkeeper_city = NPC("Innkeeper", self.NPC_spawn.NPC[3])
        self.innkeeper_village = NPC("Innkeeper", self.NPC_spawn.NPC[4])
        self.merchant_city = NPC("Merchant", self.NPC_spawn.NPC[5])
        self.merchant_village = NPC("Merchant", self.NPC_spawn.NPC[6])
        self.guard = NPC("Guard", self.NPC_spawn.NPC[7])
        self.monk = NPC("Monk", self.NPC_spawn.NPC[8])

    def choose_direction(self, x, direction):
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

    def check_if_able_to_fight(self, x, enemies_spawn):
        for i in range(len(enemies_spawn)):
            if x in enemies_spawn[i]:
                return True
        return False

