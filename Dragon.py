from Character import Character


class Dragon(Character):
    
    def __init__ (self):
        self.max_health = 200

        self.stats = {
            "name" : "dragon",
            "strength": 15,
            "health": 100.0,
        }

    def damage_player():
        pass

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print (f"Your Health is now {self.stats['health']}")
