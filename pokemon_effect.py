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


# String padding for display art
def string_padding(input):
    if len(input) == 8:
        return input
    else:
        return input.center(8)


# Battle data tracker.
def battle_data_add(battle_data, mypoke, opppoke, result):
    mypoke = string_padding(mypoke)
    opppoke = string_padding(opppoke)

    line_string = "| " + mypoke + " |  " + opppoke + " | " + result + " |"
    battle_data.append(line_string)


def battle_data_print(battle_data):
    print("-------------------------------")
    print("| Your Pick|  Opp Pick| Result|")
    print("-------------------------------")
    for x in battle_data:
        print(x)
    print("-------------------------------")


# Poke_Battle is takes values and determines appropriate response. Selects which function to call.


def poke_battle(mypoke, opppoke):

    if mypoke == "BUG":
        result = poke_bug(mypoke, opppoke)
    elif mypoke == "DARK":
        result = poke_dark(mypoke, opppoke)
    elif mypoke == "DRAGON":
        result = poke_dragon(mypoke, opppoke)
    elif mypoke == "ELECTRIC":
        result = poke_electric(mypoke, opppoke)
    elif mypoke == "FAIRY":
        result = poke_fairy(mypoke, opppoke)
    elif mypoke == "FIGHTING":
        result = poke_fighting(mypoke, opppoke)
    elif mypoke == "FIRE":
        result = poke_fire(mypoke, opppoke)
    elif mypoke == "FLYING":
        result = poke_flying(mypoke, opppoke)
    elif mypoke == "GHOST":
        result = poke_ghost(mypoke, opppoke)
    elif mypoke == "GRASS":
        result = poke_grass(mypoke, opppoke)
    elif mypoke == "GROUND":
        result = poke_ground(mypoke, opppoke)
    elif mypoke == "ICE":
        result = poke_ice(mypoke, opppoke)
    elif mypoke == "NORMAL":
        result = poke_normal(mypoke, opppoke)
    elif mypoke == "POISON":
        result = poke_poison(mypoke, opppoke)
    elif mypoke == "PSYCHIC":
        result = poke_psychic(mypoke, opppoke)
    elif mypoke == "ROCK":
        result = poke_rock(mypoke, opppoke)
    elif mypoke == "STEEL":
        result = poke_steel(mypoke, opppoke)
    elif mypoke == "WATER":
        result = poke_water(mypoke, opppoke)
    else:
        print("An Error has occured with ", opppoke)

    return result


# Beyond this point is fed into the function poke_battle() above to be called.

# Easy-mode automatic print functions


def poke_win(mypoke, opppoke):
    print("Your", mypoke, "type pokemon is strong against your opponent's",
          opppoke, "type Pokemon.\n")
    print("\nYOU WIN!!!!!!!\n")
    result = " WIN"
    return result


def poke_lose(mypoke, opppoke):
    print("Your", mypoke, "type pokemon is weak against your opponent's",
          opppoke, "type Pokemon.\n")
    print("\nYOU LOSE!!!!!!\n")
    result = "LOSE"
    return result


def poke_neutral(mypoke, opppoke):
    print(mypoke, "type and", opppoke,
          "type are neutral to each other. \nLet's flip a coin. Heads you WIN, Tails you LOSE...\n")
    coin = random.randint(1, 2)
    if coin == 1:
        print("That's heads...WOW Lucky day\nYOU WIN!!!!!!\n")
        result = " WIN"
    else:
        print("That's tails...BUMMER\nYOU LOSE!!!!!!\n")
        result = "LOSE"
    return result


# Now going over 18 types and Outcome Functions considering Dragon, Ghost, and Normal

# Bug

def poke_bug(mypoke, opppoke):
    strength = ["GRASS", "DARK", "PSYCHIC"]
    weakness = ["FIRE", "FLYING", "ROCK"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Dark


def poke_dark(mypoke, opppoke):
    strength = ["GHOST", "PSYCHIC"]
    weakness = ["BUG", "FAIRY", "FIGHTING"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Dragon - Special case Dragon would be neutral


def poke_dragon(mypoke, opppoke):
    strength = ["DRAGON"]
    weakness = ["DRAGON", "FAIRY", "ICE"]
    if opppoke in strength:
        result = poke_neutral(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Electric


def poke_electric(mypoke, opppoke):
    strength = ["FLYING", "WATER"]
    weakness = ["GROUND"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Fairy


def poke_fairy(mypoke, opppoke):
    strength = ["FIGHTING", "DARK", "DRAGON"]
    weakness = ["POISON", "STEEL"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Fighting


def poke_fighting(mypoke, opppoke):
    strength = ["DARK", "ICE", "NORMAL", "ROCK", "STEEL"]
    weakness = ["FAIRY", "FLYING", "PSYCHIC"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Fire


def poke_fire(mypoke, opppoke):
    strength = ["BUG", "GRASS", "ICE", "STEEL"]
    weakness = ["GROUND", "ROCK", "WATER"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Flying


def poke_flying(mypoke, opppoke):
    strength = ["BUG", "FIGHTING", "GRASS"]
    weakness = ["ELECTRIC", "ICE", "ROCK"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Ghost


def poke_ghost(mypoke, opppoke):
    strength = ["GHOST", "PSYCHIC"]
    weakness = ["DARK", "GHOST"]
    if opppoke in strength:
        if opppoke == "GHOST":
            result = poke_neutral(mypoke, opppoke)
        else:
            result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Grass


def poke_grass(mypoke, opppoke):
    strength = ["GROUND", "ROCK", "WATER"]
    weakness = ["BUG", "FIRE", "FLYING", "ICE", "POISON"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Ground


def poke_ground(mypoke, opppoke):
    strength = ["ELECTRIC", "FIRE", "POISON", "ROCK", "STEEL"]
    weakness = ["GRASS", "ICE", "WATER"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Ice


def poke_ice(mypoke, opppoke):
    strength = ["DRAGON", "FLYING", "GRASS", "GROUND"]
    weakness = ["FIGHTING", "FIRE", "ROCK", "STEEL"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Normal - Does not have a strength


def poke_normal(mypoke, opppoke):
    weakness = ["FIGHTING"]
    if opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Poison


def poke_poison(mypoke, opppoke):
    strength = ["FAIRY", "GRASS"]
    weakness = ["GROUND", "PSYCHIC"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result


# Psychic


def poke_psychic(mypoke, opppoke):
    strength = ["FIGHTING", "POISON"]
    weakness = ["BUG", "DARK", "GHOST"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Rock


def poke_rock(mypoke, opppoke):
    strength = ["BUG", "FIRE", "FLYING", "ICE"]
    weakness = ["FIGHTING", "GRASS", "GROUND", "STEEL", "WATER"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Steel


def poke_steel(mypoke, opppoke):
    strength = ["FAIRY", "ICE", "ROCK"]
    weakness = ["FIGHTING", "FIRE", "GROUND"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result

# Water


def poke_water(mypoke, opppoke):
    strength = ["FIRE", "GROUND", "ROCK"]
    weakness = ["ELECTRIC", "GRASS"]
    if opppoke in strength:
        result = poke_win(mypoke, opppoke)
    elif opppoke in weakness:
        result = poke_lose(mypoke, opppoke)
    else:
        result = poke_neutral(mypoke, opppoke)
    return result
