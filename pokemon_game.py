"""
Type(18)	Strong Against	                    Weakness
Bug	        Grass, Dark, Psychic	            Fire, Flying, Rock
Dark	    Ghost, Psychic	                    Bug, Fairy, Fighting
Dragon	    Dragon	                            Dragon, Fairy, Ice
Electric	Flying, Water	                    Ground
Fairy	    Fighting, Dark, Dragon	            Poison, Steel
Fighting	Dark, Ice, Normal, Rock, Steel	    Fairy, Flying, Psychic
Fire	    Bug, Grass, Ice, Steel	            Ground, Rock, Water
Flying	    Bug, Fighting, Grass	            Electric, Ice, Rock
Ghost	    Ghost, Psychic	                    Dark, Ghost
Grass	    Ground, Rock, Water	                Bug, Fire, Flying, Ice, Poison
Ground	    Electric, Fire, Poison, Rock, Steel	Grass, Ice, Water
Ice	        Dragon, Flying, Grass, Ground	    Fighting, Fire, Rock, Steel
Normal	    --	                                Fighting
Poison	    Fairy, Grass	                    Ground, Psychic
Psychic	    Fighting, Poison	                Bug, Dark, Ghost
Rock	    Bug, Fire, Flying, Ice	            Fighting, Grass, Ground, Steel, Water
Steel	    Fairy, Ice, Rock	                Fighting, Fire, Ground
Water	    Fire, Ground, Rock	                Electric, Grass
"""

import random
from pokemon_effect import *

all_poke_type = ("BUG", "DARK", "DRAGON", "ELECTRIC", "FAIRY", "FIGHTING", "FIRE", "FLYING",
                 "GHOST", "GRASS", "GROUND", "ICE", "NORMAL", "POISON", "PSYCHIC", "ROCK", "STEEL", "WATER")
# started as a list but changed to a tuple since the content never changes for better memory allocation.
# changed to a set as the order does not matter for the way I'm using to check for values which didn't work so went back to tuple


def pokegame():
    global all_poke_type

    retry_mod = ""

    battle_data = []

    while True:
        restart = input("Ready to Play" + retry_mod +
                        "! Enter 1 To Play, Enter 2 To Quit Game: ")
        if restart == "1":
            retry_mod = ", Again"
            pass
        elif restart == "2":
            break
        else:
            print("Invalid Entry")
            continue
        print("Welcome to the Pokemon Type Game!!\n")
        print("Pokemon Types:")
        print("-------------------------------")
        print("| BUG        DARK    DRAGON   |")
        print("| ELECTRIC   FAIRY   FIGHTING |")
        print("| FIRE       FLYING  GHOST    |")
        print("| GRASS      GROUND  ICE      |")
        print("| NORMAL     POISON  PSYCHIC  |")
        print("| ROCK       STEEL   WATER    |")
        print("-------------------------------")
        my_pokemon = input(
            "What is your pokemons primary type? (Only One Type): ").upper()
        if my_pokemon not in all_poke_type:
            print("This is not a known pokemon type.\nTry again!")
            continue
        opp_poke = random.choice(all_poke_type)
        print("You're opponent brought out a", opp_poke, "type pokemon.\n")
        result = poke_battle(my_pokemon, opp_poke)
        battle_data_add(battle_data, my_pokemon, opp_poke, result)
        aftergame = input(
            "Would you like to see your results? (y/n): ").lower()
        if aftergame == ("y"):
            battle_data_print(battle_data)
        else:
            print("That's fine, please play again\n")


pokegame()
