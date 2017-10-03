from random import randrange
from random import choice
from operator import neg


class MapNew:

    def __init__(self):
        self.map=[]
        for i in range(100):
            self.map.append("O")
        self.camp_gate = 0
        self.river_location = StartingTerrain.create_river(self)
        self.mountain_location = StartingTerrain.create_mountains(self)
        self.city_location = StartingTerrain.create_city(self, self.mountain_location)
        self.village_location = StartingTerrain.create_village(self, self.river_location, self.city_location)
        self.sea_location = StartingTerrain.create_sea(self, self.river_location)
        self.camp_location = StartingTerrain.create_camp_wall(self, self.village_location, self.river_location)

    def print_map(self, if_got_map):
        n = 0
        i = 0
        map_key_terrain = {0: ["Impossi", "ble to move:"], 1: ["^", "Mountains"], 2: ["=", "River"],
                        3: ["/", "Sea"], 4: ["~", "Camp's wall"]}
        map_key_enemies = {0: ["Enem", "ies:"], 1: ["w", "Wolf"], 2: ["b", "Bandit"], 3: ["s", "Skeleton"],
                   4: ["r", "Rat"]}
        map_key_misc = {6: ["x", "Your position"], 7: ["O", "Free place"], 8: ["#", "City or Village"]}
        for p in self.map:
            # check if player bought map
            if p in ["s", "r"]:
                if if_got_map == 0:
                    print("O", end=" ")
                else:
                    print(p, end=" ")
            else:
                print(p, end=" ")
            n += 1
            if n == 10:
                print("  ", end="")
                if i == 0:
                    print(map_key_terrain[i][0], end="")
                    print(map_key_terrain[i][1], end="   ")
                    print(map_key_enemies[i][0], end="")
                    print(map_key_enemies[i][1])
                if i > 0 and i < 5:
                    print(map_key_terrain[i][0], end=" - ")
                    print(map_key_terrain[i][1], end=(" " * (22 - (len(map_key_terrain[i][1]) + 4))))
                    print(map_key_enemies[i][0], end=" - ")
                    print(map_key_enemies[i][1])
                if i == 5:
                    print("")
                if i > 5 and i < 9:
                    print(map_key_misc[i][0], end=" - ")
                    print(map_key_misc[i][1],)
                i += 1
                n = 0
        print("")

class StartingTerrain:
    def create_river(self):
        river_location = randrange(4,6)
        for i in range(5):
            self.map[river_location*10+i] = "="
        sign = 1
        if river_location not in [3,4]:
            sign = neg(sign)
        for i in range(2):
            self.map[(river_location + 1 * sign) * 10 + 4 + i] = "="
        self.map[(river_location + 2 * sign) * 10 + 5] = "="
        return river_location

    def create_mountains(self):
        mountain_location = choice([0,9])
        sign = 1
        if mountain_location == 9:
            sign = neg(sign)
        for i in range(4):
            self.map[mountain_location*10+i+6] = "^"
            for k in range(3):
                self.map[(mountain_location + 1 * sign) * 10 + k + 7] = "^"
        self.map[(mountain_location + 2 * sign) * 10 + 9] = "^"
        return mountain_location

    def create_city(self, mountain_location):
        add = 0
        if mountain_location == 0:
            add = 5
        city_location = choice([0 + add,1 + add,2 + add])
        for i in range(3):
            for k in range(2):
                self.map[(city_location + i) * 10 + 8 + k] = "#"
        return city_location

    def create_village(self, river_location, city_location):
        sign = 1
        if city_location in [5,6,7]:
            sign = neg(sign)
        village_location = river_location + sign
        for i in range(3):
            self.map[(village_location) * 10 + i] = "#"
        return village_location

    def create_sea(self, river_location):
        sign = 1
        if river_location == 4:
            sign = neg(sign)
            sea_location = [9,0]
        else:
            sea_location = [0,9]
        for i in range(5):
            self.map[sea_location[0] * 10 + i] = "/"
            for k in range(3):
                self.map[(sea_location[0] + 1 * sign) * 10 + k] = "/"
        sign = neg(sign)
        for i in range(3):
            self.map[sea_location[1] * 10 + i] = "/"
        for i in range(2):
            self.map[(sea_location[1] + 1 * sign) * 10 + i] = "/"
        return sea_location

    def create_camp_wall(self, village_location, river_location):
        sign = 1
        if village_location in [5,6]:
            sign = -1
        camp_location = river_location + sign * 2
        for i in range(2):
            self.map[(camp_location) * 10 + i] = "~"
        self.map[(camp_location - sign) * 10 + 1] = "~"

        # Gate to the giant's camp
        self.camp_gate = (camp_location - sign) * 10 + 1

        camp_location = camp_location - sign

        return camp_location


