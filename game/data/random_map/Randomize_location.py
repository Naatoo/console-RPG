from random import choice


class GenerateEnemies:
    def __init__(self, mountain_location, city_location, village_location, sea_location, camp_location):
        self.enemies = [self.bandit(mountain_location=mountain_location),
                        self.skeleton(sea_location=sea_location),
                        self.rat(city_location=city_location, village_location=village_location),
                        self.giant(camp_location=camp_location)]

    @staticmethod
    def bandit(mountain_location):
        sign = -1 if mountain_location == 9 else 1
        return [(mountain_location + 1 * sign) * 10 + 6,
                *[(mountain_location + 2 * sign) * 10 + 7 + i for i in range(2)]]

    @staticmethod
    def skeleton(sea_location):
        sign = -1 if sea_location[1] == 9 else 1
        return [sea_location[1] * 10 + 3,
                *[((sea_location[1] + 1 * sign) * 10 + 2 + i) for i in range(2)]]

    @staticmethod
    def rat(city_location, village_location):
        sign = -1 if village_location in [3, 4] else 1
        return [*[(city_location + i) * 10 + 7 for i in range(3)],
                *[(village_location + sign) * 10 + i for i in range(3)]]

    @staticmethod
    def giant(camp_location):
        return [camp_location * 10]


class GenerateItemsGround:
    def __init__(self, river_location):
        self.misc = [self.reed(river_location=river_location)]

    @staticmethod
    def reed(river_location):
        sign = -1 if river_location == 5 else 1
        return [(river_location - 1 * sign) * 10 + 4,
                river_location * 10 + 5,
                (river_location + 1 * sign) * 10 + 3,
                (river_location + 1 * sign) * 10 + 6,
                (river_location + 2 * sign) * 10 + 4
                ]


class GenerateNPC:
    def __init__(self, river_location, mountain_location,
                 city_location, village_location, sea_location):
        self.NPC = []

        # Random indexes for NPC in the city
        self.NPC_in_city = []
        for i in range(3):
            for k in range(2):
                self.NPC_in_city.append((city_location + i) * 10 + 8 + k)

        # Random indexes for NPC in the village
        self.NPC_in_village = []
        for i in range(3):
            self.NPC_in_village.append(village_location * 10 + i)

        # 6 NPC in the city, 3 NPC in village
        for NPCs_nr in range(6):
            self.x_NPC_city()
        for NPCs_nr in range(3):
            self.x_NPC_village()

    def x_NPC_city(self):
        NPC_choice_temp = choice(self.NPC_in_city)
        self.NPC.append(NPC_choice_temp)
        self.NPC_in_city.remove(NPC_choice_temp)

    def x_NPC_village(self):
        NPC_choice_temp = choice(self.NPC_in_village)
        self.NPC.append(NPC_choice_temp)
        self.NPC_in_village.remove(NPC_choice_temp)
