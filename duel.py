import random


class Weapon:
    def __init__(self, weapon_name, strength):
        self.weapon_name = weapon_name
        self.strength = strength

    def __str__(self):
        return "'{weapon_name}' Weapon object (strength: {strength}).".format(weapon_name=self.weapon_name, strength=self.strength)

    def does_break(self):
        if random.random() < (self.strength / 2):
            return True
        return False


class Duelist:
    def __init__(self, duelist_name, weapon_1, weapon_2, weapon_3):
        self.duelist_name = duelist_name
        self.weapon_inventory = [weapon_1, weapon_2, weapon_3]

    def __str__(self):
        return "Duelist object '{duelist_name}', carrying {weapon_inventory[0].weapon_name}, {weapon_inventory[1].weapon_name}, and {weapon_inventory[2].weapon_name} Weapon objects.".format(duelist_name=self.duelist_name, weapon_inventory=self.weapon_inventory)

    def get_winner_of_duel_name(self, opponent):
        self_weapon = self.weapon_inventory[random.randrange(0, 3)]
        opponent_weapon = opponent.weapon_inventory[random.randrange(0, 3)]
        print("Duelist {self_name} picked a {self_weapon.weapon_name}!".format(self_name=self.duelist_name, self_weapon=self_weapon))
        print("Duelist {opponent_name} picked a {opponent_weapon.weapon_name}!".format(opponent_name=opponent.duelist_name, opponent_weapon=opponent_weapon))
        if self_weapon.strength > opponent_weapon.strength:
            if self_weapon.does_break():
                return self.duelist_name
            return opponent.duelist_name
        elif self_weapon.strength < opponent_weapon.strength:
            if opponent_weapon.does_break():
                return opponent.duelist_name
            return self.duelist_name
        elif self_weapon.strength == opponent_weapon.strength:
            print("Both duelists picked weapons of the same strength! The winner will be decided purely by pseudo-randomly generated fate!")
            coin_flip = random.randrange(0,2)
            if coin_flip == 0:
                return self.duelist_name
            return opponent.duelist_name


def main():
    """
    Sample behavior based on the README.
    """
    # Creating my Weapon objects
    weapon_1 = Weapon("Rickenbacker 4001c64", 0.8)
    weapon_2 = Weapon("Hofner 500/1", 0.6)
    weapon_3 = Weapon("Squier VI", 0.4)

    weapon_4 = Weapon("Rickenbacker 330", 0.8)
    weapon_5 = Weapon("Fender Vintera 60s Mustang", 0.6)
    weapon_6 = Weapon("Gretsch 6122", 0.4)

    # Creating my Duelist objects
    bass_player = Duelist("Aki Mizuguchi", weapon_1, weapon_2, weapon_3)
    guitarist = Duelist("Yori Asanagi", weapon_4, weapon_5, weapon_6)

    # Testing the get_winner_of_duel_name method of the Duelist object 'bass_player' a few times
    number_of_duels = 10

    for duel_number in range(number_of_duels):
        winner = bass_player.get_winner_of_duel_name(guitarist)
        print("THE WINNER OF DUEL #{} IS {}!".format(duel_number + 1, winner), end="\n\n")

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
