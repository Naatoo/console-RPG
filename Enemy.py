from Equipment import Eq


class Enemy:
    def __init__(self, name):
        # dict = {
        #   enemy: [hp, strength, agility, capacity]
        #   }
        enemies = {
            "Bandit": [500, 8, 10, 1000],
            "Skeleton": [800, 5, 6, 500],
            "Rat": [200, 4, 10, 300],
            "Giant": [2000, 40, 5, 10000],
            "Wolf": [300, 5, 8, 1000]
            }
        items = {
            "Bandit": ["Sword", "Reed"],
            "Skeleton": ["Bone Sword"],
            "Rat": ["Teeth", "Rat Fur"],
            "Giant": ["Axe"],
            "Wolf": ["Paw"],
            "Potato": ["Wolf Fur"]
            }
        self.name = name
        self.hp = enemies[name][0]
        self.strength = enemies[name][1]
        self.agility = enemies[name][2]
        self.Equipment = Eq(enemies[name][3])
        for item in items[name]:
            self.Equipment.add_element(item)


class NPC:
    def __init__(self, name, x):
        self.name = name
        items = {
            "Alchemist": ["Reed", "HP Potion", "Agility Potion", "Strength Potion"],
            "Blacksmith": ["Axe", "Silver Claymore"],
            "Cartographer": ["Axe", "Map"],
            "Innkeeper": ["Sword"],
            "Merchant": ["Sword", "HP Potion", "Bottle of Water", "Potato", "Reed"],
            "Guard": ["Axe"],
            "Monk": ["Axe"]
            }
        self.gold = 3000
        self.Equipment = Eq(100000)
        for item in items[name]:
            self.Equipment.add_element(item)
        self.x = x
        self.quest = 0
        dialogues = {
            "Alchemist": [
                0,
                                   "Hello, can you help me gathering ingredients for my new mixture?",
                                   "Please bring me 5 portions of Reed.",
                                   "You should look for it nearby the river's source.",
                                   "If you bring it to me, I will give you a bottle of my strength mixture.",
                                   1,
                                   "I am still waiting for my Reed.",
                                   "Bring it to me, please.",
                                   2,
                                   "Thank you for the Reed.",
                                   "Wait a moment for the mixture.",
                                   "Here you are.",
                                   3,
                                   "Thank you for your help.",
                                   "I hope you have drunk the mixture.",
                                   4
            ],
            "Blacksmith":
            [
                                   0,
                                   "Good morning citizen, take a look at my weapons.",
                                   1
            ],
            "Cartographer":
            [
                                    0,
                                    "Hello, don't you need a map?",
                                    1
            ],
            "Innkeeper":
            [
                                    0,
                                    "Welcome traveller. Don't you want to rest for a while?",
                                    "I can give you a bed for one night just for 20 gold.",
                                    "It can help you rest for sure.",
                                    1
            ],
            "Merchant":
            [
                                    0,
                                    "Hello, can I interest you in some of my fine wares?",
                                    1
            ],
            "Guard":
            [
                                    0,
                                    "Good morning traveller.",
                                    "Can you help me with Bandits?",
                                    "They are still and still attacking our citizens, when they travel.",
                                    "Kill all Bandits and come back to me.",
                                    "For this, you will get a brand-new weapon.",
                                    "You should find these Bandits in the mountains.",
                                    1,
                                    "You haven't killed these Bandits yet.",
                                    "Come back to me when it will be done.",
                                    2,
                                    "I heard that Bandits are already dead.",
                                    "Thank you very much.",
                                    "Here is your sword.",
                                    3,
                                    "Thanks for dealing with those Bandits.",
                                    4
            ],
            "Monk":
            [
                                    0,
                                    "Good morning, sir.",
                                    "I think that I have something that you need.",
                                    "I will give you the key to the giant's camp.",
                                    "You just need to kill one of those skeletons.",
                                    "Bring me a skeleton's sword and then the key will be yours.",
                                    "Skeletons are usually nearby the sea.",
                                    1,
                                    "Bring me the sword and then I'll give you the key.",
                                    "Look for skeletons nearby the sea.",
                                    2,
                                    "Thank you for the sword.",
                                    "Here is your key.",
                                    "On the other side of the river you can find what you looking for.",
                                    3,
                                    "I hope you can deal with this giant.",
                                    "His camp is on the other side of the rive.",
                                    4
            ]
                    }
        self.dialogues = dialogues[name]

