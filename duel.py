import random


class Weapon:
    def __init__(self, weapon_name, strength):
        self.weapon_name = weapon_name
        self.strength = strength

    def __str__(self):
        return "\'{weapon_name}\' Weapon object (strength: {strength}).".format(weapon_name=self.weapon_name, strength=self.strength)

    def does_break(self):
        if random.random() < (self.strength / 2):
            return True
        return False


class Duelist:
    pass


def main():
    """
    Sample behavior based on the README.
    """
    # Creating my Weapon objects
    test_weapon = Weapon('naginata', 0.75)
    some_weapon = Weapon("Rickenbacker 4001c64", 0.6)
    weapon_2 = Weapon("Hofner 500/1", 0.6)
    weapon_3 = Weapon("Squier VI", 0.4)

    weapon_4 = Weapon("Rickenbacker 330", 0.8)
    weapon_5 = Weapon("Fender Vintera 60s Mustang", 0.6)
    weapon_6 = Weapon("Gretsch 6122", 0.4)
    print(test_weapon)
    number_of_tests = 100
    number_of_breaks = 0

    # I'm testing this 100 times and keeping track of how many times it breaks
    for i in range(number_of_tests):
        if some_weapon.does_break():
            number_of_breaks += 1
    percentage = (number_of_breaks / number_of_tests) * 100
    print("The {} broke {}% of the time in {} tests!".format(some_weapon.weapon_name, round(percentage),
          number_of_tests))

    # Creating my Duelist objects
    # bass_player = Duelist("Aki Mizuguchi", weapon_1, weapon_2, weapon_3)
    # guitarist = Duelist("Yori Asanagi", weapon_4, weapon_5, weapon_6)
    #
    # # Testing the get_winner_of_duel_name method of the Duelist object 'bass_player' a few times
    # number_of_duels = 10
    #
    # for duel_number in range(number_of_duels):
    #     winner = bass_player.get_winner_of_duel_name(guitarist)
    #     print("THE WINNER OF DUEL #{} IS {}!".format(duel_number + 1, winner), end="\n\n")

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
