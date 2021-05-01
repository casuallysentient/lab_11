class Weapon:
    def __init__(self, weapon_name, strength):
        self.weapon_name = weapon_name
        self.strength = strength


class Duelist:
    pass


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
    print(weapon_1.weapon_name)

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
